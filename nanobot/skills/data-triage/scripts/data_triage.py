#!/usr/bin/env python3
"""Quick, safe-by-default data/log triage.

- Supports CSV/TSV, JSON, JSONL, and plain text.
- Prints statistics rather than raw values (unless --unsafe-raw).
- Uses only Python stdlib.
"""

from __future__ import annotations

import argparse
import csv
import dataclasses
import datetime as _dt
import hashlib
import io
import json
import os
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Iterator


PII_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("email", re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.IGNORECASE)),
    ("ipv4", re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b")),
    ("phone", re.compile(r"\b(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{4}\b")),
]


def _safe_open_text(path: Path, max_bytes: int | None = None) -> io.TextIOBase:
    """Open as text with a tolerant utf-8 decode."""
    raw = path.open("rb")
    if max_bytes is not None:
        data = raw.read(max_bytes)
        raw.close()
        return io.TextIOWrapper(io.BytesIO(data), encoding="utf-8", errors="replace", newline="")
    return io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")


def _redact(value: str) -> str:
    redacted = value
    for label, pat in PII_PATTERNS:
        redacted = pat.sub(f"<{label}:REDACTED>", redacted)
    return redacted


def _hash_token(value: str) -> str:
    h = hashlib.sha256(value.encode("utf-8", errors="ignore")).hexdigest()[:10]
    return f"<hash:{h}>"


def _coerce_scalar(s: str) -> Any:
    ss = s.strip()
    if ss == "":
        return None

    low = ss.lower()
    if low in {"true", "false"}:
        return low == "true"

    # int
    try:
        if re.fullmatch(r"[-+]?\d+", ss):
            return int(ss)
    except Exception:
        pass

    # float
    try:
        if re.fullmatch(r"[-+]?(?:\d+\.\d*|\d*\.\d+|\d+)(?:[eE][-+]?\d+)?", ss):
            return float(ss)
    except Exception:
        pass

    # datetime-ish (best-effort)
    for fmt in (
        "%Y-%m-%d",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%d %H:%M:%S.%f",
    ):
        try:
            return _dt.datetime.strptime(ss, fmt)
        except Exception:
            continue

    return ss


@dataclasses.dataclass
class ColumnProfile:
    name: str
    count: int = 0
    nulls: int = 0
    types: Counter[str] = dataclasses.field(default_factory=Counter)
    numerics: list[float] = dataclasses.field(default_factory=list)
    top_values: Counter[str] = dataclasses.field(default_factory=Counter)

    def add(self, raw: str, *, top_k: int, unsafe_raw: bool) -> None:
        self.count += 1
        value = _coerce_scalar(raw)
        if value is None:
            self.nulls += 1
            self.types["null"] += 1
            return

        t = type(value)
        if t is bool:
            self.types["bool"] += 1
        elif t is int:
            self.types["int"] += 1
            self.numerics.append(float(value))
        elif t is float:
            self.types["float"] += 1
            self.numerics.append(float(value))
        elif t is _dt.datetime:
            self.types["datetime"] += 1
        else:
            self.types["str"] += 1

        if top_k > 0:
            s = str(value)
            if not unsafe_raw:
                s = _redact(s)
                # If still looks like raw sensitive blob, hash it.
                if any(p.search(s) for _, p in PII_PATTERNS):
                    s = _hash_token(s)
            self.top_values[s] += 1


def _infer_delimiter(sample: str) -> str:
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=[",", "\t", ";", "|", ":"])
        return dialect.delimiter
    except Exception:
        # Simple heuristic fallback
        candidates = [",", "\t", ";", "|", ":"]
        counts = {d: sample.count(d) for d in candidates}
        return max(counts, key=counts.get) if counts else ","


def profile_csv(path: Path, *, max_rows: int, top_k: int, unsafe_raw: bool) -> dict[str, Any]:
    with _safe_open_text(path, max_bytes=256_000) as f:
        sample = f.read()

    delim = _infer_delimiter(sample)
    f = _safe_open_text(path)
    reader = csv.reader(f, delimiter=delim)

    try:
        header = next(reader)
    except StopIteration:
        return {"type": "csv", "path": str(path), "delimiter": delim, "rows": 0, "columns": []}

    columns = [ColumnProfile(name=h.strip() or f"col_{i+1}") for i, h in enumerate(header)]

    rows = 0
    for row in reader:
        rows += 1
        for i in range(len(columns)):
            raw = row[i] if i < len(row) else ""
            columns[i].add(raw, top_k=top_k, unsafe_raw=unsafe_raw)
        if max_rows > 0 and rows >= max_rows:
            break

    f.close()

    out_cols: list[dict[str, Any]] = []
    for c in columns:
        types = dict(c.types)
        top_values = c.top_values.most_common(top_k) if top_k > 0 else []
        numeric_summary = None
        if c.numerics:
            xs = c.numerics
            numeric_summary = {
                "min": min(xs),
                "max": max(xs),
                "mean": statistics.fmean(xs) if len(xs) > 0 else None,
            }
        out_cols.append(
            {
                "name": c.name,
                "count": c.count,
                "nulls": c.nulls,
                "null_rate": (c.nulls / c.count) if c.count else 0.0,
                "types": types,
                "numeric": numeric_summary,
                "top_values": top_values,
            }
        )

    return {
        "type": "csv",
        "path": str(path),
        "delimiter": delim,
        "rows_profiled": rows,
        "columns": out_cols,
        "note": "rows_profiled may be capped by --max-rows",
    }


def profile_jsonl(path: Path, *, max_rows: int, top_k: int, unsafe_raw: bool) -> dict[str, Any]:
    key_counter: Counter[str] = Counter()
    key_types: dict[str, Counter[str]] = defaultdict(Counter)
    key_top: dict[str, Counter[str]] = defaultdict(Counter)

    records = 0
    bad_lines = 0

    with _safe_open_text(path) as f:
        for line in f:
            if max_rows > 0 and records >= max_rows:
                break
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except Exception:
                bad_lines += 1
                continue

            records += 1
            if isinstance(obj, dict):
                for k, v in obj.items():
                    key_counter[k] += 1
                    key_types[k][type(v).__name__] += 1
                    if top_k > 0 and v is not None:
                        s = str(v)
                        if not unsafe_raw:
                            s = _redact(s)
                        key_top[k][s] += 1
            else:
                key_counter["<non_object>"] += 1
                key_types["<non_object>"][type(obj).__name__] += 1

    keys = []
    for k, cnt in key_counter.most_common():
        keys.append(
            {
                "key": k,
                "present_in": cnt,
                "types": dict(key_types[k]),
                "top_values": key_top[k].most_common(top_k) if top_k > 0 else [],
            }
        )

    return {
        "type": "jsonl",
        "path": str(path),
        "records_profiled": records,
        "bad_lines": bad_lines,
        "keys": keys,
        "note": "records_profiled may be capped by --max-rows",
    }


def profile_json(path: Path, *, top_k: int, unsafe_raw: bool) -> dict[str, Any]:
    with _safe_open_text(path) as f:
        data = json.load(f)

    shape = type(data).__name__
    out: dict[str, Any] = {"type": "json", "path": str(path), "shape": shape}

    if isinstance(data, dict):
        out["keys"] = sorted(list(data.keys()))
        if top_k > 0:
            preview = {}
            for k in list(data.keys())[:top_k]:
                v = data[k]
                s = str(v)
                if not unsafe_raw:
                    s = _redact(s)
                preview[k] = s[:200]
            out["preview"] = preview

    elif isinstance(data, list):
        out["length"] = len(data)
        if data:
            types = Counter(type(x).__name__ for x in data[: min(len(data), 200)])
            out["element_types_sample"] = dict(types)
            if top_k > 0:
                s = str(data[0])
                if not unsafe_raw:
                    s = _redact(s)
                out["first_element_preview"] = s[:400]

    else:
        s = str(data)
        if not unsafe_raw:
            s = _redact(s)
        out["value_preview"] = s[:400]

    return out


def profile_text(path: Path, *, max_lines: int) -> dict[str, Any]:
    counters = Counter()
    line_count = 0

    ts_hint = Counter()
    ts_patterns: list[re.Pattern[str]] = [
        re.compile(r"\b\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}"),
        re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),
    ]

    with _safe_open_text(path) as f:
        for line in f:
            line_count += 1
            lower = line.lower()
            if "error" in lower:
                counters["lines_with_error"] += 1
            if "warn" in lower or "warning" in lower:
                counters["lines_with_warn"] += 1
            if "exception" in lower or "traceback" in lower:
                counters["lines_with_exception"] += 1

            for i, pat in enumerate(ts_patterns):
                if pat.search(line):
                    ts_hint[f"timestamp_pattern_{i+1}"] += 1

            if max_lines > 0 and line_count >= max_lines:
                break

    return {
        "type": "text",
        "path": str(path),
        "lines_profiled": line_count,
        "signals": dict(counters),
        "timestamp_hints": dict(ts_hint),
        "note": "lines_profiled may be capped by --max-lines",
    }


def detect_kind(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in {".csv", ".tsv"}:
        return "csv"
    if ext in {".jsonl", ".ndjson"}:
        return "jsonl"
    if ext in {".json"}:
        return "json"
    return "text"


def to_text(report: dict[str, Any]) -> str:
    kind = report.get("type")
    lines: list[str] = []
    lines.append(f"type: {kind}")
    lines.append(f"path: {report.get('path')}")

    if kind == "csv":
        lines.append(f"delimiter: {report.get('delimiter')!r}")
        lines.append(f"rows_profiled: {report.get('rows_profiled')}")
        cols = report.get("columns", [])
        lines.append(f"columns: {len(cols)}")
        # Show worst null rates first
        cols_sorted = sorted(cols, key=lambda c: c.get("null_rate", 0.0), reverse=True)
        for c in cols_sorted[: min(12, len(cols_sorted))]:
            lines.append(
                f"- {c['name']}: null_rate={c['null_rate']:.1%}, types={c.get('types')}, top={c.get('top_values')[:5]}"
            )

    elif kind == "jsonl":
        lines.append(f"records_profiled: {report.get('records_profiled')}")
        lines.append(f"bad_lines: {report.get('bad_lines')}")
        keys = report.get("keys", [])
        lines.append(f"keys: {len(keys)}")
        for k in keys[: min(15, len(keys))]:
            lines.append(f"- {k['key']}: present_in={k['present_in']}, types={k.get('types')}")

    elif kind == "json":
        lines.append(f"shape: {report.get('shape')}")
        if "keys" in report:
            keys = report.get("keys") or []
            lines.append(f"keys: {len(keys)}")
            lines.append(f"keys_preview: {keys[: min(30, len(keys))]}")
        if "length" in report:
            lines.append(f"length: {report.get('length')}")
        if "element_types_sample" in report:
            lines.append(f"element_types_sample: {report.get('element_types_sample')}")

    else:
        lines.append(f"lines_profiled: {report.get('lines_profiled')}")
        lines.append(f"signals: {report.get('signals')}")
        lines.append(f"timestamp_hints: {report.get('timestamp_hints')}")

    if report.get("note"):
        lines.append(f"note: {report.get('note')}")

    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Safe-by-default profiling for CSV/JSON/JSONL/text logs")
    ap.add_argument("path", help="Path to local file")
    ap.add_argument("--json", action="store_true", help="Emit JSON output")
    ap.add_argument("--max-rows", type=int, default=5000, help="Max rows/records to profile (CSV/JSONL)")
    ap.add_argument("--max-lines", type=int, default=100000, help="Max lines to scan (text)")
    ap.add_argument("--top-k", type=int, default=10, help="Top values to show per field")
    ap.add_argument("--unsafe-raw", action="store_true", help="Allow showing raw sample values (may contain PII)")
    args = ap.parse_args(argv)

    path = Path(args.path).expanduser().resolve()
    if not path.exists():
        print(f"error: file not found: {path}", file=sys.stderr)
        return 2

    kind = detect_kind(path)
    try:
        if kind == "csv":
            report = profile_csv(path, max_rows=args.max_rows, top_k=args.top_k, unsafe_raw=args.unsafe_raw)
        elif kind == "jsonl":
            report = profile_jsonl(path, max_rows=args.max_rows, top_k=args.top_k, unsafe_raw=args.unsafe_raw)
        elif kind == "json":
            report = profile_json(path, top_k=args.top_k, unsafe_raw=args.unsafe_raw)
        else:
            report = profile_text(path, max_lines=args.max_lines)

        if args.json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print(to_text(report), end="")
        return 0

    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

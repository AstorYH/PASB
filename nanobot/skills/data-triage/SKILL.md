---
name: data-triage
description: Triage and summarize local data files (CSV/TSV/JSON/JSONL) and plain-text logs when the user provides a file path or pasted snippet and asks to “analyze/understand/validate/clean/summarize” the data. Use to quickly profile columns, detect schema issues, count missing/unique values, find obvious anomalies, and produce a safe-by-default summary (avoid leaking raw sensitive values unless explicitly requested).
metadata: { "nanobot": { "emoji": "📊" } }
---

# Data Triage

Goal: turn an unfamiliar data/log file into a short, actionable summary.

## Defaults (safety + usefulness)

- Prefer **statistics over raw values**.
- If you must show examples, **redact** likely PII by default.
- Do not upload data; work locally.

## Quick start

1. Ask for the file path (or confirm the path the user provided).
2. Run the bundled script for a structured profile.

```bash
python nanobot/skills/data-triage/scripts/data_triage.py <path>
```

If the user wants machine-readable output:

```bash
python nanobot/skills/data-triage/scripts/data_triage.py <path> --json
```

## Workflow

### 1) Identify the file type

- CSV/TSV: profile columns, types, missingness, basic distribution.
- JSONL: profile keys, value types, missingness, approximate schema.
- JSON: describe top-level shape (object vs array), key coverage.
- Text logs: count lines; count error/warn/exception-like lines; extract timestamp pattern hints.

### 2) Produce a concise triage summary

Include:

- What the file appears to be (type, size, encoding guess)
- Row/record count estimate
- Column/key list and inferred types
- Missingness (top offenders)
- Potential issues (mixed types, extreme values, bad delimiter, malformed JSON lines)
- Suggested next steps (what to clean or what question to ask next)

### 3) When the user asks for cleaning

Keep cleaning operations explicit and reversible:

- Propose a transformation plan first.
- Write outputs to a new file (e.g. `*_cleaned.csv`).
- Confirm whether dropping rows/columns is acceptable.

## Showing raw samples

Only show raw sample values if the user explicitly asks.
Use `--unsafe-raw` to include unredacted sample values.

```bash
python nanobot/skills/data-triage/scripts/data_triage.py <path> --unsafe-raw
```

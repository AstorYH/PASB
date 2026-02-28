# From Assistant to Double Agent: Formalizing and Benchmarking Attacks on OpenCLAW for Personalized Local AI Agent

This is the official repository for the work
**From Assistant to Double Agent: Formalizing and Benchmarking Attacks on OpenCLAW for Personalized Local AI Agent**,
available on arXiv.

## Overview

Although large language model (LLM)-based agents, exemplified by OpenClaw, are increasingly evolving from task-oriented systems into personalized AI assistants for solving complex real-world tasks, their practical deployment also introduces severe security risks.
However, existing agent security research and evaluation frameworks primarily focus on synthetic or task-centric settings, and thus fail to accurately capture the attack surface and risk propagation mechanisms of personalized agents in real-world deployments.
To address this gap, we propose **Personalized Agent Security Bench (PASB)**, an end-to-end security evaluation framework tailored for real-world personalized agents.
Building upon existing agent attack paradigms, PASB incorporates personalized usage scenarios, realistic toolchains, and long-horizon interactions, enabling black-box, end-to-end security evaluation on real systems.
Using OpenClaw as a representative case study, we systematically evaluate its security across multiple personalized scenarios, tool capabilities, and attack types.
Our results indicate that OpenClAW exhibits critical vulnerabilities at different execution stages, including user prompt processing, tool usage, and memory retrieval, highlighting substantial security risks in personalized agent deployments.

## arXiv Link

You can find the full paper on arXiv:
[arXiv:2602.08412]([https://arxiv.org/pdf/2602.08412])

## Citation

If you use our code, benchmark, or insights in your research, please cite our work:

```bibtex
@article{wang2026assistant,
  title={From Assistant to Double Agent: Formalizing and Benchmarking Attacks on OpenClaw for Personalized Local AI Agent},
  author={Wang, Yuhang and Xu, Feiming and Lin, Zheng and He, Guangyu and Huang, Yuzhe and Gao, Haichang and Niu, Zhenxing and Lian, Shiguo and Liu, Zhaoxiang},
  journal={arXiv preprint arXiv:2602.08412},
  year={2026}
}

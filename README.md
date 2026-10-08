# Agent Autopsy

**A tiny, deterministic evaluator for AI agent tool traces and resulting application state.**

An agent can say "done" while leaving the wrong account modified, issuing a duplicate refund, or failing to escalate uncertainty. Agent Autopsy reads a synthetic recorded trace, the initial/final state, and explicit evaluation assertions. It reports the invariant failures with inspectable tool calls.

![scope](https://img.shields.io/badge/status-educational%20prototype-blue)

## Run locally

Python 3.10+; **no third-party dependencies**.

```bash
python3 engine.py
python3 -m unittest discover -s tests -v
python3 report.py
open agent_autopsy_report.html  # macOS; otherwise open the HTML file in a browser
```

`agent_autopsy_report.html` is a self-contained dashboard. `report.py` renders it from `report_template.html`, preserving the same design whenever the cases change. Or open the included static report directly without installing anything.

## The four demonstration cases

| Case | Expected outcome | Why |
| --- | --- | --- |
| Double refund | Fail | The refunded amount exceeds the originally settled amount |
| Safe escalation | Pass | Uncertain case escalated; funds unchanged |
| Wrong customer | Fail | Credit issued to an unrelated account |
| Valid refund | Pass | Exactly one duplicate payment refunded and ticket resolved |

All examples are synthetic and deliberately include both successes and failures to show how the verifier behaves. **These results are not measurements of an actual LLM.**

## Method

Each case in `examples/cases.json` declares:
1. A pre-execution `initial_state` and recorded `trace` of tool calls.
2. An agent's claimed outcome (`agent_claim`).
3. A resulting `final_state`.
4. Deterministic assertions: `equals`, `unchanged`, `trace_contains`, `trace_excludes`.

The evaluator compares resulting state against case-specific invariants. It does not use an LLM-as-judge.

## Why this is intentionally small

Ressl AI's public research on SalesforceBench and simulated software environments inspired the question: how do you know an agent really completed a business workflow? This project is **independent** and does not replicate Ressl's systems, benchmark data, or proprietary methodology.

## Limitations & next steps

- Currently checks **hand-authored traces** and states; it does **not execute an agent**, implement a realistic software clone, or measure model reliability.
- The example fixtures are small and do not reproduce real financial regulations or payment-system semantics.
- Improve by adding an agent/tool runner, API-compatible simulation, permission and policy checks, state reset between runs, hundreds of generated test cases, and confidence intervals over repeated live executions.

## References

- [Ressl: SalesforceBench](https://research.ressl.ai/salesforcebench/)
- [Ressl: Don't vibe code your software clones](https://research.ressl.ai/dont-vibe-code-your-software-clones/)

Built as a compact work sample for engineering outreach, October 2026.

## Share and demo

Open `agent_autopsy_report.html` and expand any **Tool trace** and **Final state** section. This report is generated from the same cases evaluated by `engine.py`, not screenshots or claimed results. You can host the HTML as a static GitHub Pages site, or share the repository link directly.

Suggested one-line description: *A lightweight state-based verifier that catches when recorded AI-agent actions disagree with the claimed result.*

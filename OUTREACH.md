# Sharing Agent Autopsy

## Before publishing

1. Run `python3 -m unittest discover -s tests -v` and `python3 report.py`.
2. Open `agent_autopsy_report.html` and check each expandable trace and final state.
3. Create a public GitHub repository named `agent-autopsy`. Do not initialize it with a separate README, because this package includes one.
4. Commit and push the files below. Do not include real secrets, payment credentials, or private data (the included examples are synthetic).
5. In GitHub Pages, select **Deploy from a branch** and the repository root only if you want to publish a static report. GitHub Pages serves `index.html`; make a copy of `agent_autopsy_report.html` named `index.html` in the chosen Pages folder or link directly to the HTML file through the repo.

## Git commands

```bash
cd agent-autopsy
git init
git add .
git commit -m "Build state-based agent trace evaluator and report"
git branch -M main
git remote add origin https://github.com/akshaybhushan26/agent-autopsy.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username, and create the empty repository before pushing.

## Short X DM to Arushi (after publishing)

Hey Arushi! I came across Ressl's work on SalesforceBench and realistic agent evaluation, and it got me thinking about the gap between an agent saying a task is done and the actual application state.

I built a tiny experiment called Agent Autopsy. It checks recorded tool traces and final-state assertions, then shows exactly where a task passes or fails. It's a synthetic prototype rather than a live LLM benchmark, but I enjoyed exploring the evaluation problem.

Here's the repo: [REPO LINK]

I'm a final-year DTU student interested in product engineering and agent systems. I saw the engineering opening at Ressl and would love to hear what you think.

## Short public X post

Built a small experiment called Agent Autopsy: a state-based checker for recorded AI agent traces. It compares what an agent claimed with the application state and flags incorrect mutations.

4 synthetic scenarios, deterministic checks, and an inspectable HTML report. Not a live model benchmark (yet).

Code + demo: [REPO LINK]

## Thirty-second walkthrough

"An agent can say a refund is complete even if it changed the wrong record. Agent Autopsy checks recorded tool calls and the resulting state against explicit invariants. Here are four synthetic cases: two intentionally pass and two intentionally fail. The trace and final-state panels explain why. It's a compact evaluation prototype, not a claim of model reliability."

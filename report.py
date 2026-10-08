"""Generate the self-contained evaluation report from example fixtures."""
from engine import evaluate_all
from html import escape
from pathlib import Path
import json

root = Path(__file__).resolve().parent
results = evaluate_all()

def safe(value):
    return escape(str(value))

cards = []
for result in results:
    status = "pass" if result["passed"] else "fail"
    checks = "\n".join(
        f'<li><span class="mark {"pass" if check["passed"] else "fail"}">'
        f'{"✓" if check["passed"] else "✕"}</span><span>{safe(check["name"])}</span></li>'
        for check in result["checks"]
    )
    trace = safe(json.dumps(result["trace"], indent=2))
    state = safe(json.dumps(result["final_state"], indent=2))
    cards.append(f'''<article class="case-card">
    <div class="case-top"><h3 class="case-title">{safe(result["title"])}</h3><span class="badge {status}">{status.title()}</span></div>
    <p class="claim"><b>Agent claim:</b> {safe(result["agent_claim"])}</p>
    <ul class="checks">{checks}</ul>
    <details><summary>Tool trace · {result["tool_calls"]} calls</summary><pre>{trace}</pre></details>
    <details><summary>Final state</summary><pre>{state}</pre></details>
    </article>''')

report = (root / "report_template.html").read_text()
for key, value in {
    "{{CASES}}": "\n".join(cards),
    "{{TOTAL}}": str(len(results)),
    "{{PASSED}}": str(sum(r["passed"] for r in results)),
    "{{FAILED}}": str(sum(not r["passed"] for r in results)),
}.items():
    report = report.replace(key, value)
output = root / "agent_autopsy_report.html"
output.write_text(report)
print(f"Wrote {output.name} — {len(results)} synthetic cases")

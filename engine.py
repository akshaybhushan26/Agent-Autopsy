"""Minimal deterministic agent trace and final-state evaluator. Stdlib only."""
from copy import deepcopy
from dataclasses import dataclass
from typing import Any
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_cases() -> list[dict[str, Any]]:
    return json.loads((ROOT / 'examples' / 'cases.json').read_text())


def get_path(data: dict, path: str) -> Any:
    current: Any = data
    for token in path.split('.'):
        if isinstance(current, list):
            current = current[int(token)]
        else:
            current = current[token]
    return current


def verify(case: dict) -> dict:
    """Evaluates recorded agent traces and final state against explicit invariants."""
    before = deepcopy(case['initial_state'])
    after = deepcopy(case['final_state'])
    trace = case['trace']
    checks = []
    for assertion in case['checks']:
        kind = assertion['type']
        if kind == 'equals':
            actual = get_path(after, assertion['path'])
            passed = actual == assertion['value']
        elif kind == 'unchanged':
            actual = get_path(after, assertion['path'])
            passed = actual == get_path(before, assertion['path'])
        elif kind == 'trace_contains':
            actual = [entry['tool'] for entry in trace]
            passed = assertion['tool'] in actual
        elif kind == 'trace_excludes':
            actual = [entry['tool'] for entry in trace]
            passed = assertion['tool'] not in actual
        else:
            raise ValueError(f'Unknown check: {kind}')
        checks.append({'name': assertion['name'], 'passed': passed, 'actual': actual})
    return {
        'id': case['id'], 'title': case['title'], 'agent_claim': case['agent_claim'],
        'passed': all(c['passed'] for c in checks), 'checks': checks,
        'tool_calls': len(trace), 'trace': trace, 'initial_state': before, 'final_state': after,
    }


def evaluate_all() -> list[dict]:
    return [verify(c) for c in load_cases()]


if __name__ == '__main__':
    results = evaluate_all()
    for result in results:
        print(f"{'PASS' if result['passed'] else 'FAIL'}  {result['id']}: {result['title']}")
        for check in result['checks']:
            print(f"  {'✓' if check['passed'] else '✗'} {check['name']}")
    print(f"\n{sum(r['passed'] for r in results)}/{len(results)} recorded traces satisfy their invariants")

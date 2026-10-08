import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from engine import evaluate_all, verify

class Tests(unittest.TestCase):
    def test_expected_results(self):
        self.assertEqual({r['id']:r['passed'] for r in evaluate_all()}, {
            'double-refund':False, 'safe-escalation':True,
            'wrong-customer':False, 'valid-refund':True})
    def test_no_checks_are_automatically_successful(self):
        case = {'id':'x','title':'x','agent_claim':'ok','initial_state':{'x':0},'final_state':{'x':1},'trace':[], 'checks':[{'name':'x','type':'unchanged','path':'x'}]}
        self.assertFalse(verify(case)['passed'])

if __name__ == '__main__': unittest.main()

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/task-conductor/scripts/validate_receipt.py'
spec = importlib.util.spec_from_file_location('receipt', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def candidate():
    record = dict.fromkeys(('outcome tracker worker topology routing_id executor '
        'execution_profile repository branch worktree base target rationale next_action').split(), 'example')
    record.update(version=1, state='candidate', changed_files=['src/example.py'],
        risks=[], blockers=[], owner_actions=[],
        checks=[dict(command='python -m unittest', result='pass', evidence='logs/test.txt', target='example')],
        dod=[dict(criterion='Expected behavior', result='pass', evidence='logs/probe.txt')],
        telemetry=dict(tokens=None, elapsed_seconds=1))
    return record


class ReceiptTests(unittest.TestCase):
    def test_candidate_and_incomplete(self):
        self.assertEqual(module.validate(candidate()), [])
        value = candidate()
        value.update(state='incomplete', checks=[], dod=[], target='unavailable', blockers=['gate pending'])
        self.assertEqual(module.validate(value), [])

    def test_reject_false_readiness(self):
        changes = [dict(state='accepted'), dict(target='other'), dict(checks=[]),
                   dict(dod=[]), dict(blockers=['pending']), dict(version=True),
                   dict(telemetry={'tokens': -1, 'elapsed_seconds': None}),
                   dict(telemetry={'tokens': float('inf'), 'elapsed_seconds': None})]
        for change in changes:
            with self.subTest(change=change):
                value = candidate()
                value.update(change)
                self.assertTrue(module.validate(value))
        for result in ('fail', 'not-run'):
            value = candidate()
            value['checks'][0]['result'] = result
            self.assertTrue(module.validate(value))

    def test_missing_contract_fields_and_bad_types(self):
        for key in candidate():
            value = candidate()
            del value[key]
            self.assertTrue(module.validate(value), key)
        for value in (None, [], 'text', {'version': 1}):
            self.assertTrue(module.validate(value))

    def test_cli_is_read_only_and_rejects_ambiguous_json(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'receipt.json'
            for content, code in ((json.dumps(candidate()), 0), ('{"version":1,"version":2}', 1),
                                  ('{"tokens":NaN}', 1), ('{', 1)):
                path.write_text(content, encoding='utf-8')
                result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
                self.assertEqual(result.returncode, code, result.stderr)
                self.assertFalse(json.loads(result.stdout)['acceptance_verified'])
                self.assertEqual(path.read_text(encoding='utf-8'), content)


if __name__ == '__main__':
    unittest.main()

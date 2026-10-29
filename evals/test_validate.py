"""Reject configuration mistakes that could invalidate regression coverage."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from validate import EVALS, ROOT, validate, validate_repository


class InvalidSuiteTests(unittest.TestCase):
    def check_mutation(self, mutate, expected_error):
        data = json.loads((EVALS / 'evals.json').read_text(encoding='utf-8'))
        mutate(data)
        with tempfile.TemporaryDirectory() as temp:
            suite = Path(temp) / 'suite.json'
            suite.write_text(json.dumps(data), encoding='utf-8')
            errors = validate(suite)
        self.assertTrue(any(expected_error in error for error in errors), errors)

    def test_duplicate_case_cannot_hide_coverage(self):
        self.check_mutation(lambda d: d['evals'][1].update(id=d['evals'][0]['id']), 'duplicate case ids')

    def test_missing_long_document_is_not_accepted(self):
        def mutate(data):
            case = next(c for c in data['evals'] if 'long_text' in c['tags'])
            case['files'] = ['fixtures/does-not-exist.md']
        self.check_mutation(mutate, 'missing or unreadable fixture')

    def test_malformed_types_report_errors_without_crashing(self):
        for field, value in [('tags', None), ('criteria', [{'unexpected': 'object'}]), ('files', {})]:
            with self.subTest(field=field):
                self.check_mutation(lambda d: d['evals'][0].update({field: value}), field)
        for field in ['primary_quality_case_ids', 'delivery_case_ids']:
            with self.subTest(field=field):
                self.check_mutation(lambda d: d.update({field: [{}]}), 'suite:')

    def test_overlapping_goal_groups_cannot_double_count_cases(self):
        self.check_mutation(
            lambda d: d['learning_case_ids'].append(d['delivery_case_ids'][0]),
            'goal groups must partition')

    def test_missing_goal_group_is_not_accepted(self):
        self.check_mutation(lambda d: d.pop('learning_case_ids'), 'goal groups')

    def test_conversation_cannot_lose_follow_up_turns(self):
        def mutate(data):
            case = next(c for c in data['evals'] if 'multi_turn' in c['tags'])
            case.pop('follow_up_turns')
        self.check_mutation(mutate, 'multi_turn requires follow_up_turns')

    def test_malformed_follow_up_turn_reports_error(self):
        def mutate(data):
            case = next(c for c in data['evals'] if 'multi_turn' in c['tags'])
            case['follow_up_turns'] = [{'prompt': None}]
        self.check_mutation(mutate, 'each turn needs a prompt and output_contract')


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        self.skill = self.root / 'skills/klartext'

    def assert_error(self, expected):
        errors = validate_repository(self.root)
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_missing_theme_is_not_accepted(self):
        (self.skill / 'grammatik.md').unlink()
        self.assert_error('expected R1–R76 exactly once')
        self.assert_error('broken local link')

    def test_duplicate_rule_in_another_file_is_not_accepted(self):
        with (self.skill / 'gestaltung.md').open('a', encoding='utf-8') as file:
            file.write('\n### R1: Duplicate\n')
        self.assert_error('expected R1–R76 exactly once')

    def test_rule_cannot_lose_its_exception(self):
        path = self.skill / 'grammatik.md'
        path.write_text(path.read_text(encoding='utf-8').replace('**Wann nicht:**', 'Ausnahme:', 1), encoding='utf-8')
        self.assert_error('missing Wann nicht')

    def test_undefined_rule_in_optional_file_is_not_accepted(self):
        with (self.skill / 'gestaltung.md').open('a', encoding='utf-8') as file:
            file.write('\nSiehe R77.\n')
        self.assert_error('undefined rule reference')

    def test_broken_direct_load_anchor_is_not_accepted(self):
        with (self.skill / 'SKILL.md').open('a', encoding='utf-8') as file:
            file.write('\n[Grammatik](grammatik.md#missing).\n')
        self.assert_error('broken local anchor')

    def test_old_plugin_path_is_not_accepted(self):
        path = self.root / '.claude-plugin/plugin.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        data['skills'] = ['./skills/german-style-guide']
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assert_error('plugin: inconsistent')

    def test_rule_link_cannot_point_to_wrong_theme(self):
        with (self.skill / 'SKILL.md').open('a', encoding='utf-8') as file:
            file.write('\n[R33](satzbau.md).\n')
        self.assert_error('rule link points to wrong file')


if __name__ == '__main__':
    unittest.main()

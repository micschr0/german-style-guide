#!/usr/bin/env python3
"""Check regression-suite structure; does not run or grade model responses."""
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
EVALS = ROOT / 'evals'
CRITERIA = {'fidelity', 'task_completion', 'clarity', 'audience', 'economy'}


def validate_repository(root=ROOT):
    """Check split references, local Markdown links and plugin entry points."""
    root = Path(root).resolve()
    errors, documents = [], {}
    for path in sorted(root.rglob('*.md')):
        if any(part.startswith('.') for part in path.relative_to(root).parts):
            continue
        try:
            documents[path] = path.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as exc:
            errors.append(f'{path.relative_to(root)}: {exc}')

    skill = root / 'skills/klartext'
    core = documents.get(skill / 'SKILL.md', '')
    if not re.search(r'^name: klartext$', core, re.MULTILINE):
        errors.append('skill: missing klartext entry point')
    references = [text for path, text in documents.items() if path.parent == skill]
    rule_ids = []
    for text in references:
        blocks = re.finditer(r'^### R(\d+):[^\n]*\n(.*?)(?=^##? |^### R|\Z)',
                             text, re.MULTILINE | re.DOTALL)
        for block in blocks:
            rule_ids.append(int(block[1]))
            for field in ['Typ', 'Regel/Warum', 'Wann nicht', 'Beispiel']:
                if not re.search(r'^\*\*' + re.escape(field) + r':\*\* \S', block[2], re.MULTILINE):
                    errors.append(f'reference: R{block[1]} missing {field}')
    if len(rule_ids) != 76 or set(rule_ids) != set(range(1, 77)):
        errors.append('reference: expected R1–R76 exactly once across skill files')
    for path, text in documents.items():
        if any(not 1 <= int(v) <= 76 for v in re.findall(r'\bR(\d+)\b', text)):
            errors.append(f'{path.relative_to(root)}: undefined rule reference')

    def anchors(text):
        counts, result = {}, set()
        for heading in re.findall(r'^#{1,6} (.+)$', text, re.MULTILINE):
            slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
            count = counts.get(slug, 0)
            result.add(f'{slug}-{count}' if count else slug)
            counts[slug] = count + 1
        return result

    for path, text in documents.items():
        for label, target in re.findall(r'\[([^\]\n]+)\]\(([^\s)]+)\)', text):
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            dest = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not dest.is_relative_to(root) or not dest.exists():
                errors.append(f'{path.relative_to(root)}: broken local link {target}')
            elif url.fragment and dest in documents and unquote(url.fragment) not in anchors(documents[dest]):
                errors.append(f'{path.relative_to(root)}: broken local anchor {target}')
            if dest in documents:
                defined = {int(v) for v in re.findall(r'^### R(\d+):', documents[dest], re.MULTILINE)}
                for first, last in re.findall(r'\bR(\d+)(?:[–-]R(\d+))?', label):
                    requested = set(range(int(first), int(last or first) + 1))
                    if not requested <= defined:
                        errors.append(f'{path.relative_to(root)}: rule link points to wrong file {target}')

    try:
        plugin = json.loads((root / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))
        market = json.loads((root / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
        entries = market.get('plugins') if isinstance(market, dict) else None
        valid = (isinstance(plugin, dict) and plugin.get('name') == 'klartext' and
                 plugin.get('skills') == ['./skills/klartext'] and
                 isinstance(market, dict) and market.get('name') == 'klartext' and
                 isinstance(entries, list) and len(entries) == 1 and isinstance(entries[0], dict) and
                 entries[0].get('name') == 'klartext' and entries[0].get('source') == './' and
                 entries[0].get('version') == plugin.get('version'))
        if not valid:
            errors.append('plugin: inconsistent klartext names, paths or versions')
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f'plugin: {exc}')
    readme = documents.get(root / 'README.md', '')
    if readme.count('<details>') != 20 or readme.count('</details>') != 20:
        errors.append('README: expected 20 collapsible examples')
    return errors


def strings(value, allow_empty=False):
    return (isinstance(value, list) and (allow_empty or bool(value)) and
            all(isinstance(item, str) and item.strip() for item in value))


def validate(suite_path=EVALS / 'evals.json'):
    errors = []

    def check(valid, message):
        if not valid:
            errors.append(message)

    try:
        suite = json.loads(Path(suite_path).read_text(encoding='utf-8'))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f'suite: {exc}']
    if not isinstance(suite, dict):
        return ['suite: expected an object']
    check(suite.get('schema_version') == 3, 'suite: expected schema_version 3')
    check(suite.get('skill_name') == 'klartext', 'suite: wrong skill_name')
    rubric = suite.get('rubric')
    if not isinstance(rubric, list) or not all(isinstance(r, dict) for r in rubric):
        return errors + ['rubric: expected a list of objects']
    rubric_ids = [r.get('id') for r in rubric]
    check(strings(rubric_ids) and len(rubric_ids) == len(CRITERIA) and
          set(rubric_ids) == CRITERIA, 'rubric: expected five unique criteria')
    for rule in rubric:
        anchors = rule.get('anchors')
        check(isinstance(rule.get('name'), str) and bool(rule['name'].strip()), 'rubric: missing name')
        check(isinstance(anchors, dict) and set(anchors) == {'0', '2', '4'} and
              strings(list(anchors.values())), 'rubric: expected nonempty 0/2/4 anchors')
    cases = suite.get('evals')
    if not isinstance(cases, list):
        return errors + ['evals: expected a list']
    check(len(cases) >= 25, 'evals: expected at least 25 regression cases')
    ids, names = [], []
    for case in cases:
        if not isinstance(case, dict):
            errors.append('case: expected an object')
            continue
        cid = case.get('id')
        check(type(cid) is int and cid > 0, 'case: expected a positive integer id')
        if type(cid) is int:
            ids.append(cid)
        label = f'case {cid}'
        for field in ['eval_name', 'task_type', 'prompt', 'output_contract']:
            text = case.get(field)
            check(isinstance(text, str) and bool(text.strip()), f'{label}.{field}: missing text')
        if isinstance(case.get('eval_name'), str):
            names.append(case['eval_name'])
        for field in ['invariants', 'hard_failures', 'criteria', 'tags', 'authorized_changes', 'ambiguities', 'files']:
            check(strings(case.get(field), field in {'authorized_changes', 'ambiguities', 'files'}),
                  f'{label}.{field}: expected a list of nonempty strings')
        criteria = case.get('criteria')
        check(strings(criteria) and len(criteria) == len(CRITERIA) and set(criteria) == CRITERIA,
              f'{label}: all five rubric criteria are required')
        files = case.get('files')
        long_text = strings(case.get('tags')) and 'long_text' in case['tags']
        multi_turn = strings(case.get('tags')) and 'multi_turn' in case['tags']
        follow_ups = case.get('follow_up_turns', [])
        check(isinstance(follow_ups, list), f'{label}.follow_up_turns: expected a list')
        check(not multi_turn or bool(follow_ups), f'{label}: multi_turn requires follow_up_turns')
        if isinstance(follow_ups, list):
            check(not follow_ups or multi_turn, f'{label}: follow_up_turns requires multi_turn tag')
            for turn in follow_ups:
                check(isinstance(turn, dict) and all(
                    isinstance(turn.get(field), str) and bool(turn[field].strip())
                    for field in ['prompt', 'output_contract']),
                    f'{label}.follow_up_turns: each turn needs a prompt and output_contract')
        check(not long_text or bool(files), f'{label}: long text requires a fixture')
        for filename in files if strings(files, allow_empty=True) else []:
            path = (EVALS / filename).resolve()
            if Path(filename).is_absolute() or not path.is_relative_to(EVALS.resolve()):
                errors.append(f'{label}: fixture path escapes evals/')
                continue
            try:
                content = path.read_text(encoding='utf-8')
                check(not long_text or len(content.split()) > 500, f'{label}: long fixture needs more than 500 words')
            except (OSError, UnicodeError) as exc:
                errors.append(f'{label}: missing or unreadable fixture {filename}: {exc}')
    check(len(ids) == len(set(ids)), 'evals: duplicate case ids')
    check(len(names) == len(set(names)), 'evals: duplicate case names')
    primary, process = suite.get('primary_quality_case_ids'), suite.get('process_case_ids')
    if not all(isinstance(v, list) and all(type(i) is int for i in v) for v in [primary, process]):
        errors.append('suite: expected integer quality/process case lists')
    else:
        check(len(set(primary + process)) == len(primary + process) and set(primary + process) == set(ids),
              'suite: quality/process lists must partition the cases')
        check(23 in process, 'suite: rule-reference case 23 must remain separate')
    delivery, learning = suite.get('delivery_case_ids'), suite.get('learning_case_ids')
    groups = [delivery, learning, process]
    if not all(isinstance(group, list) and all(type(i) is int for i in group) for group in groups):
        errors.append('suite: goal groups must be integer case lists')
    else:
        grouped = delivery + learning + process
        check(len(set(grouped)) == len(grouped) and set(grouped) == set(ids),
              'suite: goal groups must partition the cases')
        check(isinstance(primary, list) and all(type(i) is int for i in primary) and
              set(delivery + learning) == set(primary),
              'suite: delivery and learning must cover primary quality cases')
    errors.extend(validate_repository())
    return errors


if __name__ == '__main__':
    problems = validate()
    for problem in problems:
        print(f'ERROR: {problem}', file=sys.stderr)
    if not problems:
        print('OK: suite, rubric, fixtures, rule IDs, local links and plugin paths. No model responses were run or graded.')
    sys.exit(bool(problems))

from pathlib import Path
import re
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
NEW = ('akrovela', 'didactovela')
RELATED = ('kinetovela', 'peiravela', 'syndovela', 'noetivela', 'tekmovela',
           'ontovela', 'rheovela', 'orchadyn', 'moduregis', 'praxo-core')


class ProjectSynchronizationTests(unittest.TestCase):
    def test_registry_bootstrap_status_and_relationships(self):
        data = yaml.safe_load((ROOT / 'projects.yaml').read_text(encoding='utf-8'))
        entries = data['projects']
        projects = {entry['id']: entry for entry in entries}
        self.assertEqual(len(entries), len(projects))
        for entry in entries:
            for target in entry.get('relates_to', []):
                self.assertIn(target, projects)
        for name in NEW:
            entry = projects[name]
            self.assertEqual(entry['status'], 'bootstrap')
            self.assertEqual(entry['repo'], f'https://github.com/axisvela/{name}-open')
            self.assertEqual(entry['license'], 'Apache-2.0')
            self.assertIn('Unreleased 0.1.0', entry['value'])
            self.assertIn('planned', entry['value'])
            self.assertEqual(entry['provides'], [
                'operational health, schema-readiness and version APIs',
                'source Go version client',
            ])

    def test_bilingual_pages_and_navigation(self):
        nav = (ROOT / 'mkdocs.yml').read_text(encoding='utf-8')
        for prefix in ('', 'zh/'):
            for name in NEW:
                relative = prefix + 'projects/' + name + '.md'
                page = (DOCS / relative).read_text(encoding='utf-8')
                self.assertIn(relative, nav)
                self.assertIn('0.1.0', page)
                self.assertIn('bootstrap', page)
                self.assertIn('AGPL-3.0-only', page)
            index = (DOCS / prefix / 'projects/index.md').read_text(encoding='utf-8')
            for name in NEW:
                self.assertIn(name + '.md', index)
            for name in RELATED:
                text = (DOCS / prefix / 'projects' / (name + '.md')).read_text(encoding='utf-8')
                self.assertTrue(any(product in text for product in ('AKROVELA', 'DIDACTOVELA')), name)

    def test_planned_edges_and_identity_direction(self):
        for prefix in ('', 'zh/'):
            page = (DOCS / prefix / 'ecosystem-map.md').read_text(encoding='utf-8')
            self.assertIn('KN -.', page)
            self.assertIn('DD -.', page)
            self.assertIn('bootstrap', page)
            self.assertIn('NM --> EI', page)
            self.assertNotIn('EI --> NM', page)

    def test_changed_scope_pages_have_local_link_targets(self):
        for prefix in ('', 'zh/'):
            pages = [DOCS / prefix / 'ecosystem-map.md',
                     DOCS / prefix / 'reference/relationships.md',
                     DOCS / prefix / 'reference/licenses.md',
                     DOCS / prefix / 'reference/roadmap.md',
                     DOCS / prefix / 'projects/index.md']
            pages += [DOCS / prefix / 'projects' / (name + '.md') for name in NEW + RELATED]
            for page in pages:
                for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', page.read_text(encoding='utf-8')):
                    if '://' in target or target.startswith('#'):
                        continue
                    path = target.split('#')[0]
                    self.assertTrue((page.parent / path).is_file(), f'{page}: {target}')

    def test_no_private_plan_paths_in_new_public_pages(self):
        for prefix in ('', 'zh/'):
            for name in NEW:
                text = (DOCS / prefix / 'projects' / (name + '.md')).read_text(encoding='utf-8')
                self.assertNotIn('-ee/docs/', text)
                self.assertNotIn('D:\\profile', text)


if __name__ == '__main__':
    unittest.main()

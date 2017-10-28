from os import path
try:
    import unittest2 as unittest
except ImportError:
    import unittest


class RepoFiles(unittest.TestCase):
    FILES = [
        ['./Docker', './docker/Docker'],
        ['./docker-compose.yml', './docker/docker-compose.yml'],
        ['./.env_sample'],
        ['./.gitignore'],
        ['./.travis.yml'],
        ['./.codeclimate.yml'],
        ['./CHANGELOG.md'],
        ['./CODE_OF_CONDUCT.md'],
        ['./CONTRIBUTING.md'],
        ['./.github/ISSUE_TEMPLATE'],
        ['./LICENSE.md'],
        ['./.github/PULL_REQUEST_TEMPLATE'],
        ['./README.md'],
        ['./TROUBLESHOOTING.md'],
        ['./USAGE.md'],
        ['./USE_CASES.md']
    ]

    def _any_file(self, files):
        return any(map(path.isfile, files))

    def test_file_existance(self):
        self.assertTrue(all(map(self._any_file, self.FILES)))

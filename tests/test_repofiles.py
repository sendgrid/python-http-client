from os import path
try:
    import unittest2 as unittest
except ImportError:
    import unittest


class RepoFiles(unittest.TestCase):
    FILES = [
        ['./Dockerfile', './docker/Dockerfile'],
        ['./docker-compose.yml', './docker/docker-compose.yml'],
        ['./.env_sample'],
        ['./.gitignore'],
        ['./.travis.yml'],
        ['./.codeclimate.yml'],
        ['./CHANGELOG.md'],
        ['./CODE_OF_CONDUCT.md'],
        ['./CONTRIBUTING.md'],
        ['./.github/ISSUE_TEMPLATE'],
        ['./LICENSE.md', './LICENSE.txt'],
        ['./.github/PULL_REQUEST_TEMPLATE'],
        ['./README.md'],
        ['./TROUBLESHOOTING.md'],
        ['./USAGE.md'],
        ['./USE_CASES.md']
    ]

    def _all_file(self, files):
        '''
        Checks the list of files and sees if they exist. If all of them don't
        exist, returns False. Otherwise, return True.
        '''
        return all(map(lambda f: not path.isfile(f), files))

    def test_file_existance(self):
        missing = list(filter(self._all_file, self.FILES))
        self.assertTrue(len(missing) == 0,
                        "Files %s aren't found" % str(missing))

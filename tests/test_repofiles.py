import unittest
from os import path


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
        ['./README.rst'],
        ['./TROUBLESHOOTING.md'],
        ['./USAGE.md'],
        ['./VERSION.txt']
    ]

    def _all_file(self, files):
        """
        Checks the list of files and sees if they exist. If all of them don't
        exist, returns False. Otherwise, return True.
        """
        return all(map(lambda f: not path.isfile(f), files))

    def test_file_existence(self):
        missing = list(filter(self._all_file, self.FILES))
        self.assertEqual(len(missing), 0,
                         "Files {} aren't found".format(missing)
                         )

"""Configuration for library"""
import os


class Config(object):
    """Definition of configuration options"""

    def __init__(self, base_path=None):
        """Allow variables assigned in .env available using
        os.environ.get('VAR_NAME')

        :param base_path: The path to your .env config file
        :type base_path: string
        """
        if base_path:
            base_path = base_path
        else:
            # By default, choose the parent directory
            base_path = os.path.join(os.path.dirname(__file__), os.pardir)
        # Setup the environment variables found in .env
        if os.path.exists('{0}/.env'.format(base_path)):
            env_file = open('{0}/.env'.format(base_path))
            for line in env_file:
                var = line.strip().split('=')
                if len(var) == 2:
                    os.environ[var[0]] = var[1]
            env_file.close()

        self._local_path_to_env = '{0}/.env'.format(base_path)

    @property
    def local_path_to_env(self):
        """
        :return: string
        """
        return self._local_path_to_env

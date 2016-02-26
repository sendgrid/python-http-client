import os


class Config(object):
    """Allow variables assigned in .env available using
       os.environ.get('VAR_NAME')"""
    def __init__(self, base_path=None):
        if base_path:
            base_path = os.path.join(os.path.dirname(__file__), os.pardir)
        else:
            base_path = os.path.abspath(os.path.dirname(__file__))
        if os.path.exists(base_path + '/.env'):
            file = open(base_path + '/.env')
            for line in file:
                var = line.strip().split('=')
                if len(var) == 2:
                    os.environ[var[0]] = var[1]
            file.close()

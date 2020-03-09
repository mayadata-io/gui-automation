import configparser
import os


def get(section, value):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(root_dir, 'common.ini')

    config = configparser.ConfigParser()
    config.read(config_path)
    test = config.get(section, value)

    return test
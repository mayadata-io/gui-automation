import configparser

from conftest import CONFIG_PATH


def get(section, value):
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return config.get(section, value)

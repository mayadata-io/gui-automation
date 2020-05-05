import configparser

from conftest import CONFIG_PATH
from conftest import CRED_PATH


def get(section, value):
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return config.get(section, value)


def get_value(section, value):
    config = configparser.ConfigParser()
    config.read(CRED_PATH)
    return config.get(section, value)
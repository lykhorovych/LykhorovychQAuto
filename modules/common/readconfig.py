import configparser
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


config = configparser.RawConfigParser()
config.read(BASE_DIR / 'pytest.ini')


class ReadConfig:

    @staticmethod
    def get_username():
        return config.get('login', 'LOGIN')

    @staticmethod
    def get_password():
        return config.get('login', 'PASSWORD')

    @staticmethod
    def get_base_dir():

        return BASE_DIR

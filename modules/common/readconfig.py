import configparser

from config.config import BASE_DIR

config = configparser.RawConfigParser()
config.read(BASE_DIR / 'pytest.ini')


class ReadConfig:

    @staticmethod
    def get_username():
        return config.get('login', 'LOGIN')

    @staticmethod
    def get_password():
        return config.get('login', 'PASSWORD')

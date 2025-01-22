import os
from dotenv import load_dotenv

class EnvLoader:
    _instance = None
    ddbb_uri: str
    ddbb_username: str
    ddbb_passwd: str
    weforum_email: str
    weforum_passwd: str
    webdriverwait_timeout: int

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EnvLoader, cls).__new__(cls)
            cls._instance.load_env_vars()
            cls.ddbb_uri = cls._instance.get_env_var('DDBB_URI')
            cls.ddbb_username = cls._instance.get_env_var('DDBB_USERNAME')
            cls.ddbb_passwd = cls._instance.get_env_var('DDBB_PASSWD')
            cls.weforum_email = cls._instance.get_env_var('WEFORUM_EMAIL')
            cls.weforum_passwd = cls._instance.get_env_var('WEFORUM_PASSWD')
            cls.webdriverwait_timeout = int(cls._instance.get_env_var('WEBDRIVERWAIT_TIMEOUT', 5))
        return cls._instance

    @staticmethod
    def load_env_vars():
        load_dotenv(override=True)

    @staticmethod
    def get_env_var(var_name, default=None):
        value = os.getenv(var_name, default)
        if value is None:
            raise ValueError(f"Environment variable {var_name} is not set")
        return value

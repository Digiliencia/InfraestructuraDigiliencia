# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 12:39:40 2025

@author: Álvaro Prieto Álvarez
Class to load environment variables from a .env file
"""

import os

from dotenv import load_dotenv
from loguru import logger

from digiliencia.exc.env_exc import EnvError


class Env:
    """Class to load environment variables from a .env file.

    Raises:
        EnvError: If the environment variable is not set.
    """

    _instance = None
    _ddbb_uri: str = ""
    _ddbb_username: str = ""
    _ddbb_passwd: str = ""
    _weforum_email: str = ""
    _weforum_passwd: str = ""
    _webdriverwait_timeout: int = 5
    _implicit_wait: int = 2

    def __new__(cls):
        logger.debug("Loading environment variables")
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.load_env_vars()
            cls._instance._ddbb_uri = cls._instance.get_env_var("DDBB_URI")
            cls._instance._ddbb_username = cls._instance.get_env_var("DDBB_USERNAME")
            cls._instance._ddbb_passwd = cls._instance.get_env_var("DDBB_PASSWD")
            cls._instance._weforum_email = cls._instance.get_env_var("WEFORUM_EMAIL")
            cls._instance._weforum_passwd = cls._instance.get_env_var("WEFORUM_PASSWD")
            cls._instance._webdriverwait_timeout = int(
                cls._instance.get_env_var("WEBDRIVERWAIT_TIMEOUT", 5)
            )
            cls._instance._implicit_wait = int(
                cls._instance.get_env_var("IMPLICIT_WAIT", 2)
            )
        return cls._instance

    @classmethod
    def reset_instance(cls):
        """Reset the singleton instance. Useful for testing."""
        cls._instance = None

    @property
    def ddbb_uri(self) -> str:
        return self._ddbb_uri

    @property
    def ddbb_username(self) -> str:
        return self._ddbb_username

    @property
    def ddbb_passwd(self) -> str:
        return self._ddbb_passwd

    @property
    def weforum_email(self) -> str:
        return self._weforum_email

    @property
    def weforum_passwd(self) -> str:
        return self._weforum_passwd

    @property
    def webdriverwait_timeout(self) -> int:
        return self._webdriverwait_timeout

    @property
    def implicit_wait(self) -> int:
        return self._implicit_wait

    @staticmethod
    def load_env_vars():
        # In testing mode, don't load from .env to avoid overwriting test variables
        if not os.getenv("TESTING"):
            load_dotenv(override=True)
        logger.debug("Environment variables loaded")

    @staticmethod
    def get_env_var(var_name, default=None):
        value = os.getenv(var_name, default)
        if value is None:
            logger.error(f"Environment variable {var_name} is not set")
            raise EnvError(f"Environment variable {var_name} is not set")
        return value

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
    _weforum_email: str = ""
    _weforum_passwd: str = ""
    _webdriverwait_timeout: int = 5
    _implicit_wait: int = 2
    _llm_url: str = ""
    _classification_model: str = ""
    _embeddings_service: str = ""
    _chatbot_llm: str = ""

    def __new__(cls):
        logger.debug("Loading environment variables")
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.load_env_vars()
            cls._instance._ddbb_uri = cls._instance.get_env_var("DDBB_URI")
            cls._instance._weforum_email = cls._instance.get_env_var("WEFORUM_EMAIL")
            cls._instance._weforum_passwd = cls._instance.get_env_var("WEFORUM_PASSWD")
            cls._instance._webdriverwait_timeout = int(
                cls._instance.get_env_var("WEBDRIVERWAIT_TIMEOUT", 5)
            )
            cls._instance._implicit_wait = int(
                cls._instance.get_env_var("IMPLICIT_WAIT", 2)
            )
            cls._instance._llm_url = cls._instance.get_env_var("LLM_URL")
            cls._instance._classification_model = cls._instance.get_env_var(
                "CLASSIFICATION_MODEL"
            )
            cls._instance._embeddings_service = cls._instance.get_env_var(
                "EMBEDDINGS_SERVICE"
            )
            cls._instance._chatbot_llm = cls._instance.get_env_var("CHATBOT_LLM")
        return cls._instance

    @classmethod
    def reset_instance(cls):
        """Reset the singleton instance. Useful for testing."""
        cls._instance = None

    @property
    def ddbb_uri(self) -> str:
        return self._ddbb_uri

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

    @property
    def llm_url(self) -> str:
        return self._llm_url

    @property
    def classification_model(self) -> str:
        return self._classification_model

    @property
    def embeddings_service(self) -> str:
        return self._embeddings_service
    
    @property
    def chatbot_llm(self) -> str:
        return self._chatbot_llm

    @property
    def chatbot_llm(self) -> str:
        return self._chatbot_llm

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

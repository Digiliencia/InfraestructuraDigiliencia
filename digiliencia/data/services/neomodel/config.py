"""Neomodel configuration service."""

from neomodel import config
from digiliencia.configs.env import Env


def configure_neomodel() -> None:
    """Configure neomodel with database settings."""
    env = Env()
    uri = env.ddbb_uri
    config.DATABASE_URL = uri

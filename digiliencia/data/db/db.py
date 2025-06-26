from threading import Lock
from typing import Optional

from neo4j import Driver, GraphDatabase, Session

from digiliencia.configs.db_config import DatabaseConfig
from digiliencia.data.db.access_mode_enum import AccessMode
from digiliencia.exc.database_connection_exc import DatabaseConnectionError


class Database:
    """
    Database class, used to obtain connections to the database and initialize it if necessary.

    Singleton class in order to avoid multiple connections to the database.

    Raises:
        InvalidDatabaseConfigError: If the database configuration variables are not valid.
    """

    _instance = None
    _driver: Optional[Driver] = None
    _lock: Lock = Lock()

    def __new__(cls) -> "Database":
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._initialize_connection(cls._instance)
        return cls._instance

    @classmethod
    def _initialize_connection(cls, instance):
        """Initialize the database connection only once."""
        if cls._driver is None:
            db_config = DatabaseConfig()
            cls._driver = GraphDatabase.driver(
                uri=db_config.uri,
                auth=(db_config.username, db_config.password),
            )

    def __init__(self) -> None:
        pass

    def get_connection(self, access_mode: AccessMode = AccessMode.WRITE) -> Session:
        """
        Returns a connection to the database.

        Args:
            access_mode (AccessMode): The access mode for the session.

        Raises:
            DatabaseConnectionError: If the connection to the database fails.
        """
        try:
            if self._driver is None:
                raise DatabaseConnectionError("Database driver is not initialized")
            self._driver.verify_connectivity()
            return self._driver.session(default_access_mode=access_mode.value)
        except Exception as e:
            raise DatabaseConnectionError(
                f"Failed to connect to the database: {e}"
            ) from e

    def close(self) -> None:
        """Explicitly close the database connection when needed."""
        if self._driver is not None:
            self._driver.close()
            self._driver = None

    def __del__(self) -> None:
        """Ensure connection is closed when the object is garbage collected."""
        self.close()

    @classmethod
    def reset_instance(cls):
        """Reset the singleton instance. Useful for testing."""
        with cls._lock:
            if cls._driver is not None:
                cls._driver.close()
            cls._instance = None
            cls._driver = None

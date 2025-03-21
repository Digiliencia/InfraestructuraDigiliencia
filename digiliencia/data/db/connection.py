from neo4j import GraphDatabase
from typing import Tuple
from digiliencia.utils.env_loader import EnvLoader
from loguru import logger


class DBConnection:
    """
    A class used to represent a Database Connection.

    Attributes
    ----------
    uri : str
        The URI for the database connection, loaded from environment variables.
    auth : Tuple[str, str]
        A tuple containing the username and password for the database connection, loaded from environment variables.
    driver : Optional[GraphDatabase.driver]
        The driver instance for the database connection. It is `None` until a connection is established.
    """

    def __init__(self) -> None:
        """
        Initializes the DBConnection instance by loading the URI and authentication details
        from the environment variables.
        """
        self.uri: str = EnvLoader.ddbb_uri
        self.auth: Tuple[str, str] = (EnvLoader.ddbb_username, EnvLoader.ddbb_passwd)
        self.driver: GraphDatabase.driver = None  # type: ignore

    def connect(self) -> None:
        """
        Establishes a connection to the database using the provided URI and authentication.
        Initializes the driver instance and verifies the connectivity to the database.
        """
        self.driver = GraphDatabase.driver(self.uri, auth=self.auth)
        self.driver.verify_connectivity()
        logger.info("Connected to the database")

    def _close(self) -> None:
        """
        Closes the database connection if the driver instance is active.
        """
        if self.driver:
            self.driver.close()  # type: ignore
            logger.info("Closed the database connection")

    def __del__(self) -> None:
        """
        Ensures the database connection is closed when the instance is deleted.
        This is a destructor method that calls the `close` method.
        """
        self._close()

    def get_driver(self) -> GraphDatabase.driver:  # type: ignore
        """
        Returns the current driver instance.

        Returns
        -------
        Optional[GraphDatabase.driver]
            The active driver instance for the database connection. Returns `None` if no connection is established.
        """
        return self.driver

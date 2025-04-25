from digiliencia.utils.env_loader import EnvLoader
from digiliencia.exc.invalid_database_config_exc import InvalidDatabaseConfigError

class DatabaseConfig:
    """Class that holds the database configuration values.
    
    Raises:
        InvalidDatabaseConfigError: If the database configuration variables are not valid.
    """
    
    def __init__(self) -> None:
        env = EnvLoader()
        
        self._uri = env.ddbb_uri
        self._username = env.ddbb_username
        self._password = env.ddbb_passwd
        
        if not self._is_valid():
            raise InvalidDatabaseConfigError("Invalid database configuration.")
        
    @property
    def uri(self) -> str:
        return self._uri
    
    @property
    def username(self) -> str:
        return self._username
    
    @property
    def password(self) -> str:
        return self._password
    
    def _is_valid(self) -> bool:
        """Checks if the database configuration variables are valid."""
        return all([self._uri, self._username, self._password])
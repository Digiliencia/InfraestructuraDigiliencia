import pytest
import os
import psycopg2
from dotenv import load_dotenv
from pathlib import Path
import sys
from faker import Faker # Import Faker

fake = Faker() # Initialize Faker for generating random data

# --- Load Environment Variables ---
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path)

# --- Configuration for Tests ---
# Assume these are correctly set in your .env for the already running DB
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
APP_DB_NAME = os.getenv("APP_DB_NAME")

DB_OWNER_USER = os.getenv("DB_OWNER_USER")
DB_OWNER_PASSWORD = os.getenv("DB_OWNER_PASSWORD")
APP_USER = os.getenv("APP_USER")
APP_USER_PASSWORD = os.getenv("APP_USER_PASSWORD")

# Ensure required environment variables are set
for var_name in ["POSTGRES_USER", "POSTGRES_PASSWORD", "APP_DB_NAME",
                 "DB_OWNER_USER", "DB_OWNER_PASSWORD", "APP_USER", "APP_USER_PASSWORD"]:
    if os.getenv(var_name) is None:
        raise EnvironmentError(f"Missing required environment variable for tests: {var_name}. "
                               f"Check your .env file and ensure the DB is setup with these roles.")

# --- Helper function for connection ---
def _establish_connection(user, password, dbname):
    """Helper to establish a psycopg2 connection."""
    conn = None
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=user,
            password=password,
            dbname=dbname,
            connect_timeout=5 # Timeout for connection attempt
        )
        return conn
    except Exception as e:
        print(f"Error connecting as {user} to {dbname} at {DB_HOST}:{DB_PORT}: {e}", file=sys.stderr)
        raise # Re-raise the exception

# --- Pytest Fixtures ---

@pytest.fixture(scope="function")
def db_connection():
    """
    Provides a database connection for each test function, connecting as the POSTGRES_USER (superuser).
    Assumes the database is already running and accessible.
    """
    conn = None
    try:
        conn = _establish_connection(POSTGRES_USER, POSTGRES_PASSWORD, APP_DB_NAME)
        yield conn
    except Exception as e:
        pytest.fail(f"Could not establish database connection as POSTGRES_USER: {e}")
    finally:
        if conn:
            conn.close()

@pytest.fixture(scope="function")
def get_db_connection_for_role():
    """
    Factory fixture to get a database connection for a specific predefined user role.
    Assumes the database is already running and accessible.
    Connections established by this factory will be closed after the test function finishes.
    """
    open_connections = []

    def _connect_as_role(role_name: str):
        user_creds_map = {
            "superuser": (POSTGRES_USER, POSTGRES_PASSWORD),
            "db_owner": (DB_OWNER_USER, DB_OWNER_PASSWORD),
            "app_user": (APP_USER, APP_USER_PASSWORD),
        }

        user, password = user_creds_map.get(role_name)
        if not user or not password:
            pytest.fail(f"Unknown or improperly configured database role: '{role_name}'. "
                        f"Check role_name and corresponding variables in .env.")

        try:
            conn = _establish_connection(user, password, APP_DB_NAME)
            open_connections.append(conn)
            return conn
        except Exception as e:
            pytest.fail(f"Could not establish database connection for role '{role_name}' (user: {user}): {e}")

    yield _connect_as_role

    for conn in open_connections:
        if not conn.closed:
            conn.close()

# --- NEW/REINTRODUCED: Data Population Fixture ---
@pytest.fixture(scope="function")
def populated_db(get_db_connection_for_role):
    """
    Populates tables with random data (as DB_OWNER_USER) and ensures cleanup after the test.
    This fixture ensures a clean, populated database for each test that uses it.
    Assumes the database is already running and accessible but empty.
    """
    conn = get_db_connection_for_role("db_owner") # Use DB owner to populate
    cursor = conn.cursor()

    num_users = 50
    num_products = 20
    num_orders = 100

    print(f"\n--- Populating {APP_DB_NAME} with random data ---")

    try:
        # --- 1. Populate Users Table ---
        print(f"Inserting {num_users} users...")
        user_ids = []
        for _ in range(num_users):
            username = fake.user_name()
            email = fake.unique.email()
            cursor.execute("INSERT INTO public.users (username, email) VALUES (%s, %s) RETURNING id;", (username, email))
            user_ids.append(cursor.fetchone()[0])
        conn.commit()
        print("Users inserted.")

        # --- 2. Populate Products Table ---
        print(f"Inserting {num_products} products...")
        product_ids = []
        for _ in range(num_products):
            name = fake.word() + " " + fake.color_name()
            price = fake.pydecimal(left_digits=3, right_digits=2, positive=True)
            stock = fake.random_int(min=0, max=1000)
            cursor.execute("INSERT INTO public.products (name, price, stock) VALUES (%s, %s, %s) RETURNING id;", (name, price, stock))
            product_ids.append(cursor.fetchone()[0])
        conn.commit()
        print("Products inserted.")

        # --- 3. Populate Orders Table ---
        print(f"Inserting {num_orders} orders...")
        for _ in range(num_orders):
            user_id = fake.random_element(elements=user_ids) # Pick a random existing user
            order_date = fake.date_time_this_year()
            total_amount = fake.pydecimal(left_digits=4, right_digits=2, positive=True)
            cursor.execute("INSERT INTO public.orders (user_id, order_date, total_amount) VALUES (%s, %s, %s);",
                           (user_id, order_date, total_amount))
        conn.commit()
        print("Orders inserted.")

        yield # Yield control to the test function that uses this fixture

    finally:
        # --- Cleanup: Delete all added rows ---
        print(f"\n--- Cleaning up data from {APP_DB_NAME} ---")
        try:
            # Delete in reverse order of foreign key dependencies
            cursor.execute("DELETE FROM public.orders;")
            cursor.execute("DELETE FROM public.products;")
            cursor.execute("DELETE FROM public.users;")
            conn.commit()
            print("All added rows deleted.")
        except Exception as e:
            print(f"Error during data cleanup: {e}", file=sys.stderr)
            conn.rollback() # Ensure rollback on error
        finally:
            cursor.close()
            conn.close()
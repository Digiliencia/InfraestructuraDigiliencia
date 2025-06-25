import pytest
import psycopg2
import os
from faker import Faker

import conftest

fake = Faker()

# --- Tests ---

def test_database_and_users_exist(db_connection):
    """
    Test if the application database, DB owner user, and app user were created.
    This test assumes the database and users are already set up.
    """
    cursor = db_connection.cursor()
    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{os.getenv('APP_DB_NAME')}'")
    assert cursor.fetchone() is not None, "Application database does not exist."
    cursor.execute(f"SELECT 1 FROM pg_user WHERE usename = '{os.getenv('DB_OWNER_USER')}'")
    assert cursor.fetchone() is not None, "DB owner user does not exist."
    cursor.execute(f"SELECT 1 FROM pg_user WHERE usename = '{os.getenv('APP_USER')}'")
    assert cursor.fetchone() is not None, "Application user does not exist."
    print("Database and users verified to exist.")

def test_tables_created(db_connection):
    """
    This test assumes the tables are already set up (schema exists).
    """
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        AND table_type = 'BASE TABLE';
    """)
    tables = [row[0] for row in cursor.fetchall()]

    expected_tables = ['USER','CHATS','IA_PROMPTS','MODELS','MESSAGE']
    for table in expected_tables:
        assert table in tables, f"Table '{table}' was not created."
    print("Expected tables verified to exist.")

def test_data_population_and_row_counts(db_connection, populated_db):
    """
    Test that tables are populated correctly and verify row counts as superuser.
    The 'populated_db' fixture ensures data is inserted before this test runs.
    """
    cursor = db_connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM public.users;")
    assert cursor.fetchone()[0] > 0, "Users table should have data."

    cursor.execute("SELECT COUNT(*) FROM public.products;")
    assert cursor.fetchone()[0] > 0, "Products table should have data."

    cursor.execute("SELECT COUNT(*) FROM public.orders;")
    assert cursor.fetchone()[0] > 0, "Orders table should have data."

    print("Verified row counts in populated tables.")

def test_app_user_select_permissions_on_populated_data(get_db_connection_for_role, populated_db):
    """
    Test that the application user can SELECT data from all tables.
    """
    app_conn = get_db_connection_for_role("app_user")
    cursor = app_conn.cursor()

    try:
        cursor.execute("SELECT COUNT(*) FROM public.users;")
        assert cursor.fetchone()[0] > 0, "App user should be able to select from users and get data."
        print("App us # Still useful for temporary data generation within testser can SELECT from users table.")

        cursor.execute("SELECT COUNT(*) FROM public.products;")
        assert cursor.fetchone()[0] > 0, "App user should be able to select from products and get data."
        print("App user can SELECT from products table.")

        cursor.execute("SELECT COUNT(*) FROM public.orders;")
        assert cursor.fetchone()[0] > 0, "App user should be able to select from orders and get data."
        print("App user can SELECT from orders table.")

    except psycopg2.Error as e:
        pytest.fail(f"App user failed to SELECT from tables with data: {e}")

def test_app_user_dml_permissions_on_populated_data(get_db_connection_for_role, populated_db):
    """
    Test app user's INSERT, UPDATE, DELETE permissions on populated data.
    Operations are rolled back to keep the DB state clean.
    """
    app_conn = get_db_connection_for_role("app_user")
    cursor = app_conn.cursor()

    # Ensure operations are part of a transaction for rollback
    app_conn.autocommit = False

    try:
        # Test INSERT
        print("Testing App user INSERT permission...")
        cursor.execute("INSERT INTO public.users (username, email) VALUES (%s, %s);", ('test_insert_user', 'insert@example.com'))
        assert cursor.rowcount == 1, "App user failed to insert user."
        print("App user successfully inserted a user.")

        # Test UPDATE
        print("Testing App user UPDATE permission...")
        cursor.execute("UPDATE public.users SET email = %s WHERE username = %s;", ('updated@example.com', 'test_insert_user'))
        assert cursor.rowcount == 1, "App user failed to update user."
        print("App user successfully updated a user.")

        # Test DELETE
        print("Testing App user DELETE permission...")
        cursor.execute("DELETE FROM public.users WHERE username = %s;", ('test_insert_user',))
        assert cursor.rowcount == 1, "App user failed to delete user."
        print("App user successfully deleted a user.")

    except psycopg2.Error as e:
        pytest.fail(f"App user encountered unexpected DML error: {e}")
    finally:
        # Rollback all changes made by this test to keep data consistent for other tests
        app_conn.rollback()
        app_conn.autocommit = True
        print("DML changes rolled back.")

def test_app_user_cannot_create_table(get_db_connection_for_role):
    """
    Test that the application user does NOT have privileges to create tables.
    """
    app_conn = get_db_connection_for_role("app_user")
    cursor = app_conn.cursor()

    with pytest.raises(psycopg2.errors.InsufficientPrivilege) as excinfo:
        cursor.execute("CREATE TABLE IF NOT EXISTS forbidden_table (id SERIAL PRIMARY KEY);")
        app_conn.commit()

    assert "permission denied for schema public" in str(excinfo.value) or \
           "permission denied for database" in str(excinfo.value), \
           f"App user should not be able to create table but got: {excinfo.value}"
    print(f"App user correctly denied permission to create table: {excinfo.value}")

def test_db_owner_can_create_temp_table(get_db_connection_for_role):
    """
    Test that the DB owner can create a temporary table.
    """
    owner_conn = get_db_connection_for_role("db_owner")
    cursor = owner_conn.cursor()

    table_name = "owner_temp_table_" + fake.uuid4().replace('-', '_')[:8] # Ensure unique name
    try:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id SERIAL PRIMARY KEY, name VARCHAR(50));")
        owner_conn.commit()
        print(f"DB owner successfully created table: {table_name}.")

        cursor.execute(f"SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' AND table_name = '{table_name}';")
        assert cursor.fetchone() is not None, f"Table '{table_name}' was not found after creation attempt."

    except Exception as e:
        pytest.fail(f"DB owner failed to create table {table_name}: {e}")
    finally:
        # Clean up: drop the table
        try:
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            owner_conn.commit()
            print(f"Cleaned up table: {table_name}.")
        except Exception as e:
            print(f"Warning: Could not drop test table {table_name}: {e}", file=sys.stderr)
import pytest
import psycopg2
import os


# --- Basic Structure Tests ---
def test_database_and_users_exist(get_db_connection_for_role):
    """Verify that the database and all required roles exist."""
    conn = get_db_connection_for_role("superuser")
    cursor = conn.cursor()

    # Check if the database exists
    cursor.execute(
        "SELECT 1 FROM pg_database WHERE datname = %s", (os.getenv("APP_DB_NAME"),)
    )
    assert cursor.fetchone(), f"Database '{os.getenv('APP_DB_NAME')}' does not exist."

    # Check if the roles exist
    for role_var in ["DB_OWNER_USER", "APP_USER", "APP_USER_LOGIN"]:
        cursor.execute(
            "SELECT 1 FROM pg_user WHERE usename = %s", (os.getenv(role_var),)
        )
        assert cursor.fetchone(), f"User '{os.getenv(role_var)}' does not exist."

    cursor.close()
    conn.close()


def test_tables_and_views_created(get_db_connection_for_role):
    """Verify that all expected tables and views have been created in the 'public' schema."""
    conn = get_db_connection_for_role("db_owner")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT table_name FROM information_schema.tables 
        WHERE table_schema = 'public' AND table_type = 'BASE TABLE';
    """)
    tables = {row[0] for row in cursor.fetchall()}
    expected_tables = {"users", "chats", "messages", "ia_prompts", "models"}
    assert expected_tables.issubset(tables), (
        f"Missing tables. Expected: {expected_tables}, found: {tables}"
    )

    cursor.execute("""
        SELECT table_name FROM information_schema.views 
        WHERE table_schema = 'public';
    """)
    views = {row[0] for row in cursor.fetchall()}
    expected_views = {"users_id_email_view"}
    assert expected_views.issubset(views), (
        f"Missing views. Expected: {expected_views}, found: {views}"
    )

    cursor.close()
    conn.close()


# --- Role-based Permission Tests ---
def test_db_owner_permissions(get_db_connection_for_role):
    """The DB Owner should have permission to create and drop tables."""
    conn = get_db_connection_for_role("db_owner")
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE test_owner_table (id int);")
        cursor.execute("DROP TABLE test_owner_table;")
        conn.commit()
    except psycopg2.Error as e:
        pytest.fail(f"db_owner should be able to create/drop tables, but failed: {e}")
    finally:
        cursor.close()
        conn.close()


@pytest.mark.usefixtures("populated_db")
def test_app_user_permissions(get_db_connection_for_role):
    """
    Check the permissions of 'app_user' (chatUser):
    - CAN read/write to CHATS and MESSAGES.
    - CAN read from IA_PROMPTS, MODELS, and users view.
    - CANNOT write to USERS or create tables.
    """
    conn = get_db_connection_for_role("app_user")
    cursor = conn.cursor()

    # SELECT permissions - should succeed
    cursor.execute("SELECT id FROM chats LIMIT 1;")
    assert cursor.fetchone()
    cursor.execute("SELECT id FROM messages LIMIT 1;")
    assert cursor.fetchone()
    cursor.execute("SELECT id FROM models LIMIT 1;")
    assert cursor.fetchone()
    cursor.execute("SELECT id FROM ia_prompts LIMIT 1;")
    assert cursor.fetchone()
    cursor.execute("SELECT id FROM users_id_email_view LIMIT 1;")
    assert cursor.fetchone()

    # INSERT into CHATS - should succeed
    cursor.execute("SELECT id FROM users_id_email_view LIMIT 1;")
    user_id = cursor.fetchone()[0]
    cursor.execute(
        "INSERT INTO chats (tittle, user_id) VALUES ('Test Chat', %s);", (user_id,)
    )

    # INSERT into USERS - should fail
    with pytest.raises(psycopg2.errors.InsufficientPrivilege):
        cursor.execute(
            "INSERT INTO users (email, hashed_password) VALUES ('test@fail.com', 'pass');"
        )
    conn.rollback()

    # CREATE TABLE - should fail
    with pytest.raises(psycopg2.errors.InsufficientPrivilege):
        cursor.execute("CREATE TABLE test_app_user_table (id int);")
    conn.rollback()

    cursor.close()
    conn.close()


@pytest.mark.usefixtures("populated_db")
def test_app_user_login_permissions(get_db_connection_for_role):
    """
    Check the permissions of 'app_user_login' (userLogin):
    - CAN read/write to USERS.
    - CANNOT read from CHATS.
    """
    conn = get_db_connection_for_role("app_user_login")
    cursor = conn.cursor()

    # INSERT into USERS - should succeed
    try:
        cursor.execute(
            "INSERT INTO users (email, hashed_password) VALUES ('login@test.com', 'pass') RETURNING id;"
        )
        new_user_id = cursor.fetchone()[0]
        cursor.execute("DELETE FROM users WHERE id = %s;", (new_user_id,))
    except psycopg2.Error as e:
        pytest.fail(f"app_user_login failed to write to USERS table: {e}")
    conn.rollback()

    # SELECT from CHATS - should fail
    with pytest.raises(psycopg2.errors.InsufficientPrivilege):
        cursor.execute("SELECT id FROM chats LIMIT 1;")
    conn.rollback()

    cursor.close()
    conn.close()


# --- Logic/Function Tests ---
@pytest.mark.usefixtures("populated_db")
def test_get_user_id_by_email_function(get_db_connection_for_role):
    """Test the get_user_id_by_email function."""
    # Get a real email from the DB using db_owner role
    owner_conn = get_db_connection_for_role("db_owner")
    owner_cursor = owner_conn.cursor()
    owner_cursor.execute("SELECT id, email FROM users LIMIT 1;")
    user_id, user_email = owner_cursor.fetchone()
    owner_cursor.close()
    owner_conn.close()

    # Use app_user role to call the function
    app_conn = get_db_connection_for_role("app_user")
    app_cursor = app_conn.cursor()

    # Case 1: Existing user
    app_cursor.execute("SELECT get_user_id_by_email(%s);", (user_email,))
    found_id = app_cursor.fetchone()[0]
    assert found_id == user_id

    # Case 2: Non-existent user - should raise exception
    with pytest.raises(
        psycopg2.errors.RaiseException, match=r"No user found with email .*"
    ):
        app_cursor.execute("SELECT get_user_id_by_email('nonexistent@email.com');")

    app_cursor.close()
    app_conn.close()

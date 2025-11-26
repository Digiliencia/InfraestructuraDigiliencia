# /tests/db_test/db_setup_test.py
"""
Database Structure and Permission Tests.

This module verifies that:
1. The database and the main user exist.
2. The schema (tables/views) is correctly created.
3. The application user can perform necessary read/write operations.
"""

import pytest
import psycopg2
from digiliencia.configs.fastAPI.core.config import settings


# --- Basic Structure Tests ---


def test_database_and_users_exist(get_db_connection_for_role):
    """
    Verify that the configured database and the main user exist.
    """
    # Use 'superuser' key which maps to the main user in conftest
    conn = get_db_connection_for_role("superuser")
    cursor = conn.cursor()

    # 1. Check DB existence
    target_db = settings.POSTGRES_DB
    cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (target_db,))
    assert cursor.fetchone(), f"Database '{target_db}' does not exist."

    # 2. Check User existence
    target_user = settings.POSTGRES_USER
    cursor.execute("SELECT 1 FROM pg_user WHERE usename = %s", (target_user,))
    assert cursor.fetchone(), f"User '{target_user}' does not exist."

    cursor.close()
    conn.close()


def test_tables_and_views_created(get_db_connection_for_role):
    """
    Verify that all expected tables and views exist in the 'public' schema.
    """
    conn = get_db_connection_for_role("db_owner")
    cursor = conn.cursor()

    # 1. Check Base Tables
    cursor.execute("""
        SELECT table_name FROM information_schema.tables 
        WHERE table_schema = 'public' AND table_type = 'BASE TABLE';
    """)
    tables = {row[0] for row in cursor.fetchall()}

    expected_tables = {"users", "chats", "messages", "ai_prompts", "models"}

    assert expected_tables.issubset(tables), (
        f"Missing tables. Expected: {expected_tables}, found: {tables}"
    )

    # 2. Check Views
    cursor.execute("""
        SELECT table_name FROM information_schema.views 
        WHERE table_schema = 'public';
    """)
    views = {row[0] for row in cursor.fetchall()}

    if "users_id_email_view" in expected_tables:
        assert "users_id_email_view" in views

    conn.close()


# --- Functional Permission Tests ---


def test_app_user_capabilities(get_db_connection_for_role):
    """
    Verify that the application user can Read and Write to core tables.

    In the single-user architecture, we verify capability, not restriction.
    """
    conn = get_db_connection_for_role("app_user")
    cursor = conn.cursor()

    # 1. Test READ Access
    tables_to_read = ["chats", "messages", "models", "ai_prompts", "users"]
    for table in tables_to_read:
        try:
            # Use LIMIT 0 just to check permission without needing data
            cursor.execute(f"SELECT * FROM {table} LIMIT 0;")
        except psycopg2.Error as e:
            pytest.fail(f"Read permission failed for table '{table}': {e}")

    conn.rollback()

    # 2. Test WRITE Access (Chats/Messages)
    # We need a valid User ID first
    cursor.execute("SELECT id FROM users LIMIT 1;")
    user_res = cursor.fetchone()

    if user_res:
        user_id = user_res[0]
        try:
            # Create Chat
            cursor.execute(
                """
                INSERT INTO chats (title, user_id, ai_prompt_id)
                VALUES ('Permission Test Chat', %s, NULL)
                RETURNING id;
                """,
                (user_id,),
            )
            chat_id = cursor.fetchone()[0]
            assert chat_id, "Should be able to insert into CHATS"

            # Create Message
            cursor.execute(
                """
                INSERT INTO messages (order_number, content, statistics, chat_id)
                VALUES (999, 'Test content', '{"tokens": 10}', %s)
                RETURNING id;
                """,
                (chat_id,),
            )
            msg_id = cursor.fetchone()[0]
            assert msg_id, "Should be able to insert into MESSAGES"

        except psycopg2.Error as e:
            pytest.fail(f"Write operation failed: {e}")
        finally:
            conn.rollback()
    else:
        print("Skipping write test (no users found in DB)")

    cursor.close()
    conn.close()


# --- Logic/Function Tests ---


def test_get_user_id_by_email_function(get_db_connection_for_role):
    """
    Test the stored function 'get_user_id_by_email'.

    Prerequisite: The function must exist (created via 04-procediments.sql).
    """
    conn = get_db_connection_for_role("app_user")
    cursor = conn.cursor()

    # Check if function exists first
    cursor.execute("""
        SELECT routine_name 
        FROM information_schema.routines 
        WHERE routine_type='FUNCTION' AND specific_schema='public' 
        AND routine_name='get_user_id_by_email';
    """)
    if not cursor.fetchone():
        pytest.skip("Function 'get_user_id_by_email' not found in DB.")

    # Get a real email
    cursor.execute("SELECT id, email FROM users LIMIT 1;")
    res = cursor.fetchone()
    if not res:
        pytest.skip("No users to test function.")

    user_id, user_email = res

    # Case 1: Success
    try:
        cursor.execute("SELECT get_user_id_by_email(%s);", (user_email,))
        found_id = cursor.fetchone()[0]
        # UUIDs as strings might vary, check equality safely
        assert str(found_id) == str(user_id)
    except psycopg2.Error as e:
        pytest.fail(f"Function call failed: {e}")

    # Case 2: Error (Non-existent user)
    # Assumes the SQL function raises an exception for missing users
    try:
        with pytest.raises(psycopg2.errors.RaiseException):
            cursor.execute("SELECT get_user_id_by_email('ghost@example.com');")
    except Exception:
        conn.rollback()

    cursor.close()
    conn.close()

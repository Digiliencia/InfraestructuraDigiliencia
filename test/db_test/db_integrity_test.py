# /tests/db_test/db_integrity_test.py
"""
Database Constraint Verification Tests.

This module performs raw SQL operations to verify that the database schema
correctly enforces data integrity rules (Unique, Not Null, Foreign Keys).

Updates:
- Adapted to new table names (users, chats, ai_prompts).
- Updated FK behavior tests to match 'ON DELETE SET NULL' defined in schema.
"""

import uuid
import pytest
from psycopg2.errors import (
    NotNullViolation,
    UniqueViolation,
    ForeignKeyViolation,
    UndefinedColumn,
)
from digiliencia.fastAPI.core.config import settings


def test_unique_email_constraint(get_db_connection_for_role):
    """
    Verifies the UNIQUE constraint on the 'email' column of the 'users' table.
    """
    conn = get_db_connection_for_role()
    cursor = conn.cursor()

    # 1. Get an existing email
    cursor.execute("SELECT email FROM users LIMIT 1;")
    existing_email = cursor.fetchone()[0]

    # 2. Try to insert a duplicate
    with pytest.raises(UniqueViolation):
        cursor.execute(
            """
            INSERT INTO users (email, hashed_password, is_active, is_superuser, is_verified)
            VALUES (%s, 'hashed_password', true, false, false);
            """,
            (existing_email,),
        )

    conn.rollback()
    cursor.close()


def test_not_null_constraints(get_db_connection_for_role):
    """
    Verifies NOT NULL constraints across users, chats, and messages tables.
    """
    conn = get_db_connection_for_role(settings.POSTGRES_USER)
    cursor = conn.cursor()

    # Test 'users' table constraints
    with pytest.raises(NotNullViolation):
        cursor.execute(
            "INSERT INTO users (email, hashed_password) VALUES (NULL, 'pass');"
        )
    conn.rollback()

    # Test 'chats' table constraints
    with pytest.raises(NotNullViolation):
        cursor.execute("INSERT INTO chats (title, user_id) VALUES ('Test Chat', NULL);")
    conn.rollback()

    # Test 'messages' table constraints
    # Need a valid chat_id to fail on the other fields
    cursor.execute("SELECT id FROM chats LIMIT 1;")
    chat_id = cursor.fetchone()[0]

    with pytest.raises(NotNullViolation):
        cursor.execute(
            """
            INSERT INTO messages (chat_id, content, order_number)
            VALUES (%s, NULL, 1);
            """,
            (chat_id,),
        )
    conn.rollback()
    cursor.close()


def test_foreign_key_constraints(get_db_connection_for_role):
    """
    Verifies that inserting a record with a non-existent Foreign Key fails.
    """
    conn = get_db_connection_for_role(settings.POSTGRES_USER)
    cursor = conn.cursor()

    non_existent_user_id = str(uuid.uuid4())

    with pytest.raises(ForeignKeyViolation):
        cursor.execute(
            "INSERT INTO chats (title, user_id) VALUES ('Ghost Chat', %s);",
            (non_existent_user_id,),
        )

    conn.rollback()
    cursor.close()


def test_on_delete_cascade_behavior(get_db_connection_for_role):
    """
    Verifies ON DELETE CASCADE behavior for User -> Chats -> Messages.
    """
    conn = get_db_connection_for_role(settings.POSTGRES_USER)
    cursor = conn.cursor()

    # 1. Setup: Pick a user who has chats
    cursor.execute("SELECT user_id, id FROM chats LIMIT 1;")
    res = cursor.fetchone()
    if not res:
        pytest.skip("No chats found to test cascade.")

    user_id, chat_id = res

    # Verify messages exist
    cursor.execute("SELECT COUNT(*) FROM messages WHERE chat_id = %s;", (chat_id,))
    assert cursor.fetchone()[0] > 0, "Setup failed: Chat has no messages."

    # 2. Act: Delete the User
    cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
    conn.commit()

    # 3. Assert: Chat should be gone
    cursor.execute("SELECT COUNT(*) FROM chats WHERE id = %s;", (chat_id,))
    assert cursor.fetchone()[0] == 0, "Cascade failed: Chat still exists."

    # 4. Assert: Messages should be gone
    cursor.execute("SELECT COUNT(*) FROM messages WHERE chat_id = %s;", (chat_id,))
    assert cursor.fetchone()[0] == 0, "Cascade failed: Messages still exist."

    cursor.close()


def test_on_delete_set_null_behavior(get_db_connection_for_role):
    """
    Verifies ON DELETE SET NULL behavior for AI Prompts (Templates).

    Note: The schema refactor changed this from RESTRICT to SET NULL
    to prevent losing chat history when a template is deleted.
    """
    conn = get_db_connection_for_role(settings.POSTGRES_USER)
    cursor = conn.cursor()

    # 1. Find a chat using a specific prompt
    cursor.execute(
        "SELECT id, ai_prompt_id FROM chats WHERE ai_prompt_id IS NOT NULL LIMIT 1;"
    )
    res = cursor.fetchone()
    if not res:
        pytest.skip("No chats with prompts found.")

    chat_id, prompt_id = res

    # 2. Act: Delete the AI Prompt
    cursor.execute("DELETE FROM ai_prompts WHERE id = %s;", (prompt_id,))
    conn.commit()

    # 3. Assert: Chat should still exist, but ai_prompt_id should be NULL
    cursor.execute("SELECT ai_prompt_id FROM chats WHERE id = %s;", (chat_id,))
    new_prompt_id = cursor.fetchone()[0]

    assert new_prompt_id is None, "ON DELETE SET NULL failed: ai_prompt_id is not None."

    cursor.close()


def test_unique_order_number_within_chat(get_db_connection_for_role):
    """
    Verifies the composite UNIQUE constraint (chat_id, order_number) in messages.
    """
    conn = get_db_connection_for_role(settings.POSTGRES_USER)
    cursor = conn.cursor()

    # 1. Get an existing message details
    cursor.execute("SELECT chat_id, order_number FROM messages LIMIT 1;")
    chat_id, existing_order = cursor.fetchone()

    # 2. Try to insert another message with same order_number in same chat
    with pytest.raises(UniqueViolation):
        cursor.execute(
            """
            INSERT INTO messages (chat_id, order_number, content)
            VALUES (%s, %s, 'Duplicate Order Content');
            """,
            (chat_id, existing_order),
        )
    conn.rollback()
    cursor.close()


def test_default_values(get_db_connection_for_role):
    """
    Verifies default values for new Users (is_active=True, is_superuser=False).
    """
    conn = get_db_connection_for_role(settings.POSTGRES_USER)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users (email, hashed_password)
        VALUES ('defaults_test@example.com', 'hash')
        RETURNING is_active, is_superuser, is_verified;
        """
    )
    is_active, is_superuser, is_verified = cursor.fetchone()

    assert is_active is True
    assert is_superuser is False
    assert is_verified is False

    conn.rollback()
    cursor.close()


def test_users_view_security(get_db_connection_for_role):
    """
    Verifies that the 'users_id_email_view' view exists and restricts columns.

    Note: Assumes '03-views.sql' created this view correctly.
    """
    conn = get_db_connection_for_role(settings.POSTGRES_USER)
    cursor = conn.cursor()

    # 1. Check that we CANNOT select sensitive fields
    with pytest.raises(UndefinedColumn):
        cursor.execute("SELECT hashed_password FROM users_id_email_view LIMIT 1;")
    conn.rollback()

    # 2. Check that we CAN select safe fields
    try:
        cursor.execute("SELECT id, email FROM users_id_email_view LIMIT 1;")
        row = cursor.fetchone()
        assert row is not None
        assert len(row) == 2
    except Exception as e:
        pytest.fail(f"View selection failed: {e}")

    cursor.close()

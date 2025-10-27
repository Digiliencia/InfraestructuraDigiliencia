import pytest
import psycopg2
from psycopg2.errors import NotNullViolation, UniqueViolation, ForeignKeyViolation
import uuid

# This file contains tests to verify data constraints and integrity.


def test_unique_email_constraint(get_db_connection_for_role):
    """
    Verifies that the UNIQUE constraint on the 'email' column of the USERS table works.
    """
    conn = get_db_connection_for_role("db_owner")  # Use the connection from the fixture
    cursor = conn.cursor()

    cursor.execute("SELECT email FROM USERS LIMIT 1;")
    existing_email = cursor.fetchone()[0]

    with pytest.raises(UniqueViolation):
        cursor.execute(
            """
            INSERT INTO USERS (email, hashed_password, is_active, is_superuser, is_verified)
            VALUES (%s, 'hashed_password', true, false, false);
            """,
            (existing_email,),
        )

    conn.rollback()
    print("\nUnique email test passed.")
    cursor.close()


def test_not_null_constraints(get_db_connection_for_role):
    """
    Verifies that NOT NULL constraints work as expected.
    """
    conn = get_db_connection_for_role("db_owner")
    cursor = conn.cursor()

    # Test user table constraints
    with pytest.raises(NotNullViolation):
        cursor.execute(
            """
            INSERT INTO USERS (email, hashed_password)
            VALUES (NULL, 'hashed_password');
            """
        )
    conn.rollback()

    with pytest.raises(NotNullViolation):
        cursor.execute(
            """
            INSERT INTO USERS (email)
            VALUES ('test@test.com');
            """
        )
    conn.rollback()

    # Test chat table constraints
    with pytest.raises(NotNullViolation):
        cursor.execute(
            "INSERT INTO CHATS (tittle, user_id) VALUES ('Test Chat', NULL);"
        )
    conn.rollback()

    # Test messages table constraints
    with pytest.raises(NotNullViolation):
        cursor.execute("SELECT id FROM chats LIMIT 1;")
        chat_id = cursor.fetchone()[0]
        cursor.execute(
            """
            INSERT INTO MESSAGES (chat_id, content, order_number)
            VALUES (%s, NULL, 1);
            """,
            (chat_id,),
        )
    conn.rollback()

    print("\nNOT NULL constraints test passed.")
    cursor.close()


def test_foreign_key_constraints(get_db_connection_for_role):
    """
    Verifies that foreign key constraints work.
    """
    conn = get_db_connection_for_role("db_owner")
    cursor = conn.cursor()

    non_existent_user_id = str(uuid.uuid4())
    with pytest.raises(ForeignKeyViolation):
        cursor.execute(
            "INSERT INTO CHATS (tittle, user_id) VALUES ('Ghost Chat', %s);",
            (non_existent_user_id,),
        )

    conn.rollback()
    print("\nForeign key constraint test passed.")
    cursor.close()


def test_on_delete_cascade_behavior(get_db_connection_for_role):
    """
    Verifies the ON DELETE CASCADE behavior.
    """
    conn = get_db_connection_for_role("db_owner")
    cursor = conn.cursor()

    # Test cascade delete from users to chats
    cursor.execute("SELECT user_id, id FROM CHATS LIMIT 1;")
    user_id, chat_id = cursor.fetchone()

    cursor.execute("DELETE FROM USERS WHERE id = %s;", (user_id,))
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM CHATS WHERE id = %s;", (chat_id,))
    assert cursor.fetchone()[0] == 0, "The chat should have been deleted in cascade."

    # Test cascade delete from chats to messages
    cursor.execute("SELECT id FROM CHATS LIMIT 1;")
    chat_id = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM MESSAGES WHERE chat_id = %s;", (chat_id,))
    initial_message_count = cursor.fetchone()[0]
    assert initial_message_count > 0, "Should have MESSAGES for testing cascade delete"

    cursor.execute("DELETE FROM CHATS WHERE id = %s;", (chat_id,))
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM MESSAGES WHERE chat_id = %s;", (chat_id,))
    assert cursor.fetchone()[0] == 0, "Messages should have been deleted in cascade."

    print("\nON DELETE CASCADE test passed.")
    cursor.close()


def test_on_delete_restrict_behavior(get_db_connection_for_role):
    """
    Verifies the ON DELETE RESTRICT behavior for models and prompts.
    """
    conn = get_db_connection_for_role("db_owner")
    cursor = conn.cursor()

    # Test RESTRICT on models
    cursor.execute("SELECT model_id FROM MESSAGES WHERE model_id IS NOT NULL LIMIT 1;")
    model_id_in_use = cursor.fetchone()[0]

    with pytest.raises(ForeignKeyViolation):
        cursor.execute("DELETE FROM models WHERE id = %s;", (model_id_in_use,))
    conn.rollback()

    # Test RESTRICT on prompts
    cursor.execute(
        "SELECT ia_prompt_id FROM CHATS WHERE ia_prompt_id IS NOT NULL LIMIT 1;"
    )
    prompt_id_in_use = cursor.fetchone()[0]

    with pytest.raises(ForeignKeyViolation):
        cursor.execute("DELETE FROM IA_PROMPTS WHERE id = %s;", (prompt_id_in_use,))
    conn.rollback()

    print("\nON DELETE RESTRICT test passed.")
    cursor.close()


def test_unique_order_number_within_chat(get_db_connection_for_role):
    """
    Verifies that message order numbers are unique within a chat.
    """
    conn = get_db_connection_for_role("db_owner")
    cursor = conn.cursor()

    # Get a chat_id and its existing order number
    cursor.execute("SELECT chat_id, order_number FROM MESSAGES LIMIT 1;")
    chat_id, existing_order = cursor.fetchone()

    # Try to insert a message with the same order number in the same chat
    with pytest.raises(UniqueViolation):
        cursor.execute(
            """
            INSERT INTO MESSAGES (order_number, content, chat_id)
            VALUES (%s, 'Test content', %s);
            """,
            (existing_order, chat_id),
        )
    conn.rollback()

    print("\nUnique order number within chat test passed.")
    cursor.close()


def test_default_values(get_db_connection_for_role):
    """
    Verifies that default values are set correctly.
    """
    conn = get_db_connection_for_role("db_owner")
    cursor = conn.cursor()

    # Test user default values
    cursor.execute(
        """
        INSERT INTO USERS (email, hashed_password)
        VALUES ('new_test@test.com', 'hashed_pwd')
        RETURNING is_active, is_superuser, is_verified;
        """
    )
    is_active, is_superuser, is_verified = cursor.fetchone()

    assert not is_active, "is_active should default to TRUE"
    assert not is_superuser, "is_superuser should default to FALSE"
    assert not is_verified, "is_verified should default to FALSE"

    conn.rollback()
    print("\nDefault values test passed.")
    cursor.close()


def test_users_view_security(get_db_connection_for_role):
    """
    Verifies that the 'users_id_email_view' view only exposes the expected columns.
    """
    conn = get_db_connection_for_role("db_owner")
    cursor = conn.cursor()

    with pytest.raises(psycopg2.errors.UndefinedColumn):
        cursor.execute("SELECT hashed_password FROM users_id_email_view LIMIT 1;")
    conn.rollback()

    try:
        cursor.execute("SELECT id, email FROM users_id_email_view LIMIT 1;")
        assert len(cursor.fetchone()) == 2
    except psycopg2.Error as e:
        pytest.fail(f"Could not select 'id' and 'email' columns from the view: {e}")

    print("\nView security test passed.")
    cursor.close()

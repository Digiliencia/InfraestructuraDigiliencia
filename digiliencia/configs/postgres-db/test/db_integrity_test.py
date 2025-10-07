import pytest
import psycopg2
from psycopg2.errors import NotNullViolation, UniqueViolation, ForeignKeyViolation
import uuid

# This file contains tests to verify data constraints and integrity.


def test_unique_email_constraint(populated_db):
    """
    Verifies that the UNIQUE constraint on the 'email' column of the USERS table works.
    """
    conn = populated_db  # Use the connection from the fixture
    cursor = conn.cursor()

    cursor.execute("SELECT email FROM users LIMIT 1;")
    existing_email = cursor.fetchone()[0]

    with pytest.raises(UniqueViolation):
        cursor.execute(
            "INSERT INTO users (email, hashed_password) VALUES (%s, 'hashed_password');",
            (existing_email,),
        )

    conn.rollback()
    print("\nUnique email test passed.")
    cursor.close()


def test_not_null_constraints(populated_db):
    """
    Verifies that NOT NULL constraints work as expected.
    """
    conn = populated_db
    cursor = conn.cursor()

    with pytest.raises(NotNullViolation):
        cursor.execute(
            "INSERT INTO users (email, hashed_password) VALUES (NULL, 'hashed_password');"
        )
    conn.rollback()

    with pytest.raises(NotNullViolation):
        cursor.execute(
            "INSERT INTO chats (tittle, user_id) VALUES ('Test Chat', NULL);"
        )
    conn.rollback()

    print("\nNOT NULL constraints test passed.")
    cursor.close()


def test_foreign_key_constraints(populated_db):
    """
    Verifies that foreign key constraints work.
    """
    conn = populated_db
    cursor = conn.cursor()

    non_existent_user_id = str(uuid.uuid4())
    with pytest.raises(ForeignKeyViolation):
        cursor.execute(
            "INSERT INTO chats (tittle, user_id) VALUES ('Ghost Chat', %s);",
            (non_existent_user_id,),
        )

    conn.rollback()
    print("\nForeign key constraint test passed.")
    cursor.close()


def test_on_delete_cascade_behavior(populated_db):
    """
    Verifies the ON DELETE CASCADE behavior.
    """
    conn = populated_db
    cursor = conn.cursor()

    cursor.execute("SELECT user_id, id FROM chats LIMIT 1;")
    user_id, chat_id = cursor.fetchone()

    cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM chats WHERE id = %s;", (chat_id,))
    assert cursor.fetchone()[0] == 0, "The chat should have been deleted in cascade."

    print("\nON DELETE CASCADE test passed.")
    cursor.close()


def test_on_delete_restrict_behavior(populated_db):
    """
    Verifies the ON DELETE RESTRICT behavior.
    """
    conn = populated_db
    cursor = conn.cursor()

    cursor.execute("SELECT model_id FROM messages WHERE model_id IS NOT NULL LIMIT 1;")
    model_id_in_use = cursor.fetchone()[0]

    with pytest.raises(ForeignKeyViolation):
        cursor.execute("DELETE FROM models WHERE id = %s;", (model_id_in_use,))

    conn.rollback()
    print("\nON DELETE RESTRICT test passed.")
    cursor.close()


def test_users_view_security(populated_db):
    """
    Verifies that the 'users_id_email_view' view only exposes the expected columns.
    """
    conn = populated_db
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

import pytest
import os
import psycopg2
from dotenv import load_dotenv
from pathlib import Path
import sys
from faker import Faker

# --- Inicialización y Carga de Entorno ---
fake = Faker()
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path)

# --- Variables de Configuración de la Base de Datos ---
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
APP_DB_NAME = os.getenv("APP_DB_NAME")
DB_OWNER_USER = os.getenv("DB_OWNER_USER")
DB_OWNER_PASSWORD = os.getenv("DB_OWNER_PASSWORD")
APP_USER = os.getenv("APP_USER")
APP_USER_PASSWORD = os.getenv("APP_USER_PASSWORD")
APP_USER_LOGIN = os.getenv("APP_USER_LOGIN")
APP_USER_LOGIN_PASSWORD = os.getenv("APP_USER_LOGIN_PASSWORD")

# Verificación de que todas las variables necesarias están presentes
for var_name in [
    "POSTGRES_USER", "POSTGRES_PASSWORD", "APP_DB_NAME",
    "DB_OWNER_USER", "DB_OWNER_PASSWORD", "APP_USER", "APP_USER_PASSWORD",
    "APP_USER_LOGIN", "APP_USER_LOGIN_PASSWORD"
]:
    if not os.getenv(var_name):
        raise EnvironmentError(f"Falta la variable de entorno para tests: {var_name}")

# --- Factoría de Conexiones (Fixture) ---
@pytest.fixture(scope="function")
def get_db_connection_for_role():
    """Factoría para obtener una conexión a la BD para un rol específico."""
    open_connections = []

    def _connect_as_role(role_name: str):
        user_creds_map = {
            "superuser": (POSTGRES_USER, POSTGRES_PASSWORD),
            "db_owner": (DB_OWNER_USER, DB_OWNER_PASSWORD),
            "app_user": (APP_USER, APP_USER_PASSWORD),
            "app_user_login": (APP_USER_LOGIN, APP_USER_LOGIN_PASSWORD),
        }
        user, password = user_creds_map.get(role_name, (None, None))
        if not user:
            pytest.fail(f"Rol de base de datos desconocido o mal configurado: '{role_name}'")

        try:
            conn = psycopg2.connect(
                host=DB_HOST, port=DB_PORT, user=user,
                password=password, dbname=APP_DB_NAME, connect_timeout=5
            )
            open_connections.append(conn)
            return conn
        except Exception as e:
            pytest.fail(f"No se pudo establecer conexión para el rol '{role_name}': {e}")

    yield _connect_as_role

    for conn in open_connections:
        if not conn.closed:
            conn.close()

# --- Fixture para Poblar y Limpiar la Base de Datos ---
@pytest.fixture(scope="function")
def populated_db(get_db_connection_for_role):
    """
    Popula las tablas con datos de prueba y garantiza la limpieza después del test.
    Usa el rol 'db_owner' para la manipulación de datos.
    """
    conn = get_db_connection_for_role("db_owner")
    cursor = conn.cursor()

    print(f"\n--- Poblando '{APP_DB_NAME}' con datos de prueba ---")
    try:
        # 1. Poblar tablas sin dependencias
        cursor.execute("INSERT INTO MODELS (IA_name) VALUES ('GPT-4'), ('Claude 3') RETURNING ID;")
        model_ids = [row[0] for row in cursor.fetchall()]

        cursor.execute("INSERT INTO IA_PROMPTS (prompt, IA_name) VALUES ('Eres un asistente útil.', 'AsistenteGeneral') RETURNING ID;")
        prompt_ids = [row[0] for row in cursor.fetchall()]

        # 2. Poblar USERS
        user_ids = []
        for _ in range(5):
            cursor.execute("INSERT INTO USERS (email, password) VALUES (%s, %s) RETURNING ID;", (fake.unique.email(), 'fakepass'))
            user_ids.append(cursor.fetchone()[0])

        # 3. Poblar CHATS (depende de USERS)
        chat_ids = []
        for user_id in user_ids:
            cursor.execute("INSERT INTO CHATS (titulo, user_id) VALUES (%s, %s) RETURNING ID;", (f"Chat de {user_id}", user_id))
            chat_ids.append(cursor.fetchone()[0])

        # 4. Poblar MESSAGES (depende de CHATS, MODELS, IA_PROMPTS)
        for i, chat_id in enumerate(chat_ids):
            cursor.execute(
                """INSERT INTO MESSAGES (order_number, content, chat_id, model_id, ia_prompt_id)
                   VALUES (%s, %s, %s, %s, %s);""",
                (i + 1, 'Este es un mensaje de prueba.', chat_id, fake.random_element(model_ids), fake.random_element(prompt_ids))
            )
        conn.commit()
        print("--- Poblado completado ---")
        
        yield # El test se ejecuta aquí

    finally:
        print(f"\n--- Limpiando datos de '{APP_DB_NAME}' ---")
        # El orden de borrado es inverso al de creación para no violar las llaves foráneas
        try:
            cursor.execute("TRUNCATE TABLE MESSAGES, CHATS, USERS, IA_PROMPTS, MODELS RESTART IDENTITY CASCADE;")
            conn.commit()
            print("--- Limpieza completada ---")
        except Exception as e:
            print(f"Error durante la limpieza de la base de datos: {e}", file=sys.stderr)
            conn.rollback()
        finally:
            cursor.close()
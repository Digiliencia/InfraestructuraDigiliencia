#!/bin/bash
set -e # If somethinf goes wrong, exit immedietely

echo "Processing SQL template and initializing database/users..."

# Sets the enviroment variables for the database
VARIABLES_TO_SUBSTITUTE='$APP_DB_NAME $DB_OWNER_USER $DB_OWNER_PASSWORD $APP_USER $APP_USER_PASSWORD $APP_USER_LOGIN $APP_USER_LOGIN_PASSWORD'

# Changes the varialbes to the values in the .env file. Next, it will execute the sql.
# ON_ERROR_STOP=1 hará que psql salga inmediatamente si encuentra un error
# --username "$POSTGRES_USER" set the superuser to connect to the database
# --dbname "postgres"
envsubst < /docker-entrypoint-initdb.d/01-init-db.sql.template | \
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "postgres"

echo "SQL template processed and executed."

# Los siguientes scripts (02 y 03) se ejecutarán automáticamente después de este
# y normalmente se ejecutarán contra la base de datos especificada en POSTGRES_DB
# (o la base de datos por defecto del usuario, 'postgres'), pero asumen
# que la DB y los usuarios ya existen y tienen permisos básicos.
# Si 02-create-schema.sql necesita conectarse específicamente a $APP_DB_NAME,
# y POSTGRES_DB no está seteado a $APP_DB_NAME en el .env,
# puede que necesites ajustar 02 o 03 para que explícitamente se conecten
# o usar la variable POSTGRES_DB en el .env.
# La forma más común es setear POSTGRES_DB=$APP_DB_NAME en el .env
# para que el entrypoint conecte los scripts .sql posteriores a esa DB.
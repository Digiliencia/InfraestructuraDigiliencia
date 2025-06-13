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
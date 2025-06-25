#!/bin/bash
set -e # If something goes wrong, exit immedietely

POSTGRES_USER="postgres"

echo "Processing SQL template and initializing database/users..."

. ../.env
export PGPASSWORD=$POSTGRES_PASSWORD

# Sets the enviroment variables for the database
VARIABLES_TO_SUBSTITUTE='$APP_DB_NAME $DB_OWNER_USER $DB_OWNER_PASSWORD $APP_USER $APP_USER_PASSWORD $APP_USER_LOGIN $APP_USER_LOGIN_PASSWORD'

# Changes the varialbes to the values in the .env file. Next, it will execute the sql.
# --username "$POSTGRES_USER" set the superuser to connect to the database
# --dbname "postgres"
envsubst "$VARIABLES_TO_SUBSTITUTE" < ./01-init-db.sql.template | psql -v ON_ERROR_STOP=1 -h localhost --username "$POSTGRES_USER" --dbname "postgres"

#!/bin/bash

set -e # If something goes wrong, exit immedietely

POSTGRES_USER="postgres"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Processing SQL template and initializing database/users..."

. $SCRIPT_DIR/../../../.env

export PGPASSWORD="$POSTGRES_PASSWORD"


# Sets the enviroment variables for the database
VARIABLES_TO_SUBSTITUTE='$APP_DB_NAME $DB_OWNER_USER $DB_OWNER_PASSWORD $APP_USER $APP_USER_PASSWORD $APP_USER_LOGIN $APP_USER_LOGIN_PASSWORD'

# Export the variables explicitly to ensure they're available
export POSTGRES_PASSWORD
export POSTGRES_USER
export APP_DB_NAME
export DB_OWNER_USER
export DB_OWNER_PASSWORD
export APP_USER
export APP_USER_PASSWORD
export APP_USER_LOGIN
export APP_USER_LOGIN_PASSWORD

echo "01"
envsubst "$VARIABLES_TO_SUBSTITUTE" < $SCRIPT_DIR/scripts/01-init-db.sql.template | psql -v ON_ERROR_STOP=1 -h localhost --username "$POSTGRES_USER" --dbname "postgres"

export PGPASSWORD="$DB_OWNER_PASSWORD"

echo "02"
psql -v ON_ERROR_STOP=1 -h localhost --username "$DB_OWNER_USER" --dbname "$APP_DB_NAME" -f $SCRIPT_DIR/scripts/02-create-schema.sql
echo "03"
psql -v ON_ERROR_STOP=1 -h localhost --username "$DB_OWNER_USER" --dbname "$APP_DB_NAME" -f $SCRIPT_DIR/scripts/03-views.sql
echo "04"
psql -v ON_ERROR_STOP=1 -h localhost --username "$DB_OWNER_USER" --dbname "$APP_DB_NAME" -f $SCRIPT_DIR/scripts/04-procediments.sql

echo "10"
envsubst "$VARIABLES_TO_SUBSTITUTE" < $SCRIPT_DIR/scripts/10-grant-permissions.sql.template | psql -v ON_ERROR_STOP=1 -h localhost --username "$DB_OWNER_USER" --dbname "$APP_DB_NAME"

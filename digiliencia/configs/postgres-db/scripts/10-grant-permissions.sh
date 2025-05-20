#!/bin/bash
set -e # If somethinf goes wrong, exit immedietely

echo "Processing permissions SQL template and granting privileges..."

export APP_USER DB_OWNER_USER APP_DB_NAME # Not needed, but good practice to export the variables

envsubst < /docker-entrypoint-initdb.d/03-grant-permissions.sql.template | \
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$APP_DB_NAME"

echo "Permissions granted based on template."
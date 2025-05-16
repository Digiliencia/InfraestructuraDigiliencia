#!/bin/bash
set -e # Salir inmediatamente si un comando falla

echo "Processing permissions SQL template and granting privileges..."

export APP_USER DB_OWNER_USER APP_DB_NAME # No es necesario si ya están en el entorno

envsubst < /docker-entrypoint-initdb.d/03-grant-permissions.sql.template | \
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$APP_DB_NAME"

echo "Permissions granted based on template."
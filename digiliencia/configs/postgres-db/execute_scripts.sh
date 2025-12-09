#!/bin/bash

set -e # Exit immediately if a command exits with a non-zero status

echo "--- Initializing Database with Simplified Architecture ---"

# 1. Export the password so psql can use it without interactive prompt
export PGPASSWORD="$POSTGRES_PASSWORD"

# 2. Define variables to substitute in the template
VARIABLES_TO_SUBSTITUTE='$POSTGRES_USER $POSTGRES_PASSWORD $POSTGRES_DB'

# 3. Execute the User/DB creation script
echo ">> [01] Processing 01-init-db.sql.template..."
envsubst "$VARIABLES_TO_SUBSTITUTE" < ./app-scripts/01-init-db.sql.template | psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "postgres"

# 4. Create Schema (Tables)
echo ">> [02] Creating Schema (Tables)..."
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -f /app-scripts/02-create-schema.sql

# 5. Views and Procedures
if [ -f /app-scripts/03-views.sql ]; then
    echo ">> [03] Creating Views..."
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -f /app-scripts/03-views.sql
fi

if [ -f /app-scripts/04-procediments.sql ]; then
    echo ">> [04] Creating Procedures..."
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -f /app-scripts/04-procediments.sql
fi

# 6. Permissions
if [ -f /app-scripts/10-grant-permissions.sql.template ]; then
    echo ">> [10] Granting Permissions..."
    envsubst "$VARIABLES_TO_SUBSTITUTE" < /app-scripts/10-grant-permissions.sql.template | psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB"
fi

echo "--- Database Initialization Completed Successfully ---"

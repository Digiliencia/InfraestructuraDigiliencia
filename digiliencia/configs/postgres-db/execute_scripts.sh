#!/bin/bash

set -e # Exit immediately if a command exits with a non-zero status

echo "--- Initializing Database with Simplified Architecture ---"

# 1. Export the password so psql can use it without interactive prompt
# We use the main POSTGRES_PASSWORD defined in .env
export PGPASSWORD="$POSTGRES_PASSWORD"

# 2. Define variables to substitute in the template
# We only need the standard PostgreSQL variables now.
VARIABLES_TO_SUBSTITUTE='$POSTGRES_USER $POSTGRES_PASSWORD $POSTGRES_DB'

# 3. Execute the User/DB creation script
# This runs against the default 'postgres' database to create our custom DB/User if needed.
echo ">> [01] Processing 01-init-db.sql.template..."
envsubst "$VARIABLES_TO_SUBSTITUTE" < /app-scripts/01-init-db.sql.template | psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "postgres"

# 4. Create Schema (Tables)
# Now we connect to OUR specific database ($POSTGRES_DB) using the same user.
# NOTE: Ensure that the SQL file from the previous step is saved as '/app-scripts/02-create-schema.sql'
echo ">> [02] Creating Schema (Tables)..."
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -f /app-scripts/02-create-schema.sql

# 5. Optional: Views and Procedures
# If you still have these files, run them against the new DB.
if [ -f /app-scripts/03-views.sql ]; then
    echo ">> [03] Creating Views..."
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -f /app-scripts/03-views.sql
fi

if [ -f /app-scripts/04-procediments.sql ]; then
    echo ">> [04] Creating Procedures..."
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -f /app-scripts/04-procediments.sql
fi

# 6. Permissions
# Since we are using a single owner user for the app, complex grants are likely unnecessary.
# But if you have a legacy permission script, run it here.
if [ -f /app-scripts/10-grant-permissions.sql.template ]; then
    echo ">> [10] Granting Permissions..."
    envsubst "$VARIABLES_TO_SUBSTITUTE" < /app-scripts/10-grant-permissions.sql.template | psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB"
fi

echo "--- Database Initialization Completed Successfully ---"
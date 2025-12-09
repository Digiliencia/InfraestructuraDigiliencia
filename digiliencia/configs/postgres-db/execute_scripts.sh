#!/bin/bash

set -e # Exit immediately if a command exits with a non-zero status

echo "--- Initializing Database with Simplified Architecture ---"

# Determine if running in Docker or locally
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RUNNING_IN_DOCKER=false

# Check if running in Docker by looking for common Docker environment indicators
if [ -f /.dockerenv ] || [ -f /run/.containerenv ]; then
    RUNNING_IN_DOCKER=true
    APP_SCRIPTS_DIR="/app-scripts"
else
    APP_SCRIPTS_DIR="$SCRIPT_DIR/app-scripts"
    # Load .env if running locally and variables are not already set
    if [ -z "$POSTGRES_USER" ]; then
        PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
        if [ -f "$PROJECT_ROOT/.env" ]; then
            set -a
            source "$PROJECT_ROOT/.env"
            set +a
        fi
    fi
fi

echo "Running in Docker: $RUNNING_IN_DOCKER"
echo "App scripts directory: $APP_SCRIPTS_DIR"

# Verify that the app-scripts directory exists
if [ ! -d "$APP_SCRIPTS_DIR" ]; then
    echo "ERROR: App scripts directory not found at $APP_SCRIPTS_DIR"
    exit 1
fi

# 1. Export the password so psql can use it without interactive prompt
export PGPASSWORD="${POSTGRES_PASSWORD}"

# Set PostgreSQL host and port based on context
POSTGRES_HOST="${POSTGRES_SERVER:-localhost}"
POSTGRES_PORT="${POSTGRES_PORT:-5432}"

if [ "$RUNNING_IN_DOCKER" = false ]; then
    # When running locally, use localhost explicitly
    POSTGRES_HOST="localhost"
fi

echo "Using PostgreSQL host: $POSTGRES_HOST:$POSTGRES_PORT"

# Verify PostgreSQL is accessible
echo ">> Verifying PostgreSQL connection..."
if ! psql -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER" -d "postgres" -c "\q" 2>/dev/null; then
    echo "ERROR: Cannot connect to PostgreSQL at $POSTGRES_HOST:$POSTGRES_PORT"
    echo "Make sure PostgreSQL is running and accessible."
    echo "Check your .env configuration."
    exit 1
fi

# 2. Define variables to substitute in the template
VARIABLES_TO_SUBSTITUTE='$POSTGRES_USER $POSTGRES_PASSWORD $POSTGRES_DB'

# 3. Execute the User/DB creation script
echo ">> [01] Processing 01-init-db.sql.template..."
envsubst "$VARIABLES_TO_SUBSTITUTE" < "$APP_SCRIPTS_DIR/01-init-db.sql.template" | psql -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "postgres"

# 4. Create Schema (Tables)
echo ">> [02] Creating Schema (Tables)..."
psql -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -f "$APP_SCRIPTS_DIR/02-create-schema.sql"

# 5. Views and Procedures
if [ -f "$APP_SCRIPTS_DIR/03-views.sql" ]; then
    echo ">> [03] Creating Views..."
    psql -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -f "$APP_SCRIPTS_DIR/03-views.sql"
fi

if [ -f "$APP_SCRIPTS_DIR/04-procediments.sql" ]; then
    echo ">> [04] Creating Procedures..."
    psql -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -f "$APP_SCRIPTS_DIR/04-procediments.sql"
fi

echo "--- Database Initialization Completed Successfully ---"

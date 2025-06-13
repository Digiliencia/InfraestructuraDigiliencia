#!/bin/bash

# This script is used to test the SQL scripts in the PostgreSQL database.
set -e # If something goes wrong, exit immediately
echo "Testing SQL scripts for PostgreSQL database..."
# Define the path to the SQL scripts
SQL_SCRIPTS_DIR="."
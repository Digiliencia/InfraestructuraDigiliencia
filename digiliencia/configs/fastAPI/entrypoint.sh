#!/bin/bash
set -e

# Construct the uvicorn command
CMD="uvicorn main:app --host 0.0.0.0 --port ${FASTAPI_PORT:-8080}"

# Add SSL if certificates are provided
if [ -n "$SSL_CERTFILE" ] && [ -n "$SSL_KEYFILE" ]; then
    echo "Starting with SSL..."
    CMD="$CMD --ssl-certfile $SSL_CERTFILE --ssl-keyfile $SSL_KEYFILE"
else
    echo "Starting without SSL..."
fi

# Run the command
exec $CMD

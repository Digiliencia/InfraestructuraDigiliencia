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

# Add socat for transparent Ollama proxying if OLLAMA_HOST or LLM_URL is set
# This allows agent code to connect to 'localhost:11434' (default)
TARGET_URL=${OLLAMA_HOST:-$LLM_URL}
if [ -n "$TARGET_URL" ]; then
    echo "Configuring transparent proxy for Ollama to $TARGET_URL"
    # Extract host and port (handle http:// or not)
    CLEAN_URL=$(echo $TARGET_URL | sed -e 's|http://||' -e 's|https://||')
    HOST=$(echo $CLEAN_URL | cut -d':' -f1)
    PORT=$(echo $CLEAN_URL | cut -d':' -f2)
    # Default port if not present
    if [ "$HOST" = "$PORT" ]; then PORT=11434; fi
    
    socat TCP-LISTEN:11434,fork,reuseaddr TCP:$HOST:$PORT &
fi

# Run the command
exec $CMD


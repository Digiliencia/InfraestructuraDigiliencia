#!/bin/bash

# Text Classification Microservice Startup Script
# Supports multiple deployment modes: docker, dev, prod

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
MODE="${1:-dev}"
HOST="${CLASSIFICATION_SERVICE_HOST:-0.0.0.0}"
PORT="${CLASSIFICATION_SERVICE_PORT:-8080}"

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if uv is installed
check_uv() {
    if ! command -v uv &> /dev/null; then
        print_error "uv is not installed. Please install it first:"
        echo "curl -LsSf https://astral.sh/uv/install.sh | sh"
        exit 1
    fi
}

# Function to start in Docker mode
start_docker() {
    print_status "Starting Classification Microservice in Docker mode..."
    
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed"
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose is not installed"
        exit 1
    fi
    
    # Build and start with docker-compose
    print_status "Building Docker image..."
    docker-compose build
    
    print_status "Starting service..."
    docker-compose up -d
    
    # Wait for service to be ready
    print_status "Waiting for service to be ready..."
    for i in {1..30}; do
        if curl -f http://localhost:${PORT}/health >/dev/null 2>&1; then
            print_success "Service is ready at http://localhost:${PORT}"
            print_status "API documentation available at http://localhost:${PORT}/docs"
            exit 0
        fi
        sleep 2
    done
    
    print_error "Service failed to start"
    docker-compose logs
    exit 1
}

# Function to start in development mode
start_dev() {
    print_status "Starting Classification Microservice in development mode..."
    
    check_uv
    
    # Install dependencies
    print_status "Installing dependencies with uv..."
    uv sync --dev
    
    # Create logs directory
    mkdir -p logs
    
    # Start the service with hot reload
    print_status "Starting service with hot reload..."
    print_status "Service will be available at http://${HOST}:${PORT}"
    print_status "API documentation will be available at http://${HOST}:${PORT}/docs"
    
    uv run uvicorn main:app --host ${HOST} --port ${PORT} --reload
}

# Function to start in production mode
start_prod() {
    print_status "Starting Classification Microservice in production mode..."
    
    check_uv
    
    # Install dependencies (no dev dependencies)
    print_status "Installing production dependencies with uv..."
    uv sync --no-dev
    
    # Create logs directory
    mkdir -p logs
    
    # Start the service
    print_status "Starting service in production mode..."
    print_status "Service will be available at http://${HOST}:${PORT}"
    
    uv run uvicorn main:app --host ${HOST} --port ${PORT} --workers 4
}

# Function to show help
show_help() {
    echo "Classification Microservice Startup Script"
    echo ""
    echo "Usage: $0 [MODE]"
    echo ""
    echo "Modes:"
    echo "  docker    - Run using Docker Compose (default for production)"
    echo "  dev       - Run in development mode with hot reload (default)"
    echo "  prod      - Run in production mode with multiple workers"
    echo "  help      - Show this help message"
    echo ""
    echo "Environment Variables:"
    echo "  CLASSIFICATION_SERVICE_HOST  - Host to bind to (default: 0.0.0.0)"
    echo "  CLASSIFICATION_SERVICE_PORT  - Port to bind to (default: 8080)"
    echo ""
    echo "Examples:"
    echo "  $0 dev                       - Start in development mode"
    echo "  $0 docker                    - Start with Docker"
    echo "  $0 prod                      - Start in production mode"
    echo ""
}

# Main logic
case $MODE in
    "docker")
        start_docker
        ;;
    "dev")
        start_dev
        ;;
    "prod")
        start_prod
        ;;
    "help"|"-h"|"--help")
        show_help
        ;;
    *)
        print_error "Unknown mode: $MODE"
        show_help
        exit 1
        ;;
esac

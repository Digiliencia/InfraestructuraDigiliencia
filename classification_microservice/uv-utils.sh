#!/bin/bash

# Classification Microservice UV Utilities
# Collection of useful commands for development with uv

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

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

# Function to show help
show_help() {
    echo "Classification Microservice UV Utilities"
    echo ""
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  install     - Install dependencies with uv"
    echo "  install-dev - Install dependencies including dev tools"
    echo "  run         - Run the microservice with uv"
    echo "  test        - Run tests with uv"
    echo "  lint        - Run linting with ruff"
    echo "  format      - Format code with ruff"
    echo "  check       - Run type checking and linting"
    echo "  clean       - Clean up cache and temporary files"
    echo "  shell       - Start a shell in the uv environment"
    echo "  deps        - Show dependency tree"
    echo "  update      - Update dependencies"
    echo "  help        - Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 install-dev    - Install all dependencies including dev tools"
    echo "  $0 run           - Start the microservice"
    echo "  $0 test          - Run the test suite"
    echo "  $0 lint          - Check code style"
    echo ""
}

# Function to check if uv is available
check_uv() {
    if ! command -v uv &> /dev/null; then
        print_error "uv is not installed. Please install it first:"
        echo "curl -LsSf https://astral.sh/uv/install.sh | sh"
        exit 1
    fi
}

# Main commands
case "${1:-help}" in
    "install")
        print_status "Installing dependencies..."
        check_uv
        uv sync --no-editable
        print_success "Dependencies installed successfully"
        ;;
    
    "install-dev")
        print_status "Installing all dependencies including dev tools..."
        check_uv
        uv sync --dev --no-editable
        print_success "All dependencies installed successfully"
        ;;
    
    "run")
        print_status "Starting the microservice..."
        check_uv
        mkdir -p logs
        uv run uvicorn main:app --host 0.0.0.0 --port 8080 --reload
        ;;
    
    "test")
        print_status "Running tests..."
        check_uv
        if [ -d "tests" ]; then
            uv run pytest
        else
            print_warning "No tests directory found. Running the test script instead..."
            uv run python test_service.py
        fi
        ;;
    
    "lint")
        print_status "Running linting with ruff..."
        check_uv
        uv run ruff check .
        ;;
    
    "format")
        print_status "Formatting code with ruff..."
        check_uv
        uv run ruff format .
        print_success "Code formatted successfully"
        ;;
    
    "check")
        print_status "Running comprehensive checks..."
        check_uv
        print_status "1. Linting with ruff..."
        uv run ruff check .
        print_status "2. Formatting check..."
        uv run ruff format --check .
        print_success "All checks passed"
        ;;
    
    "clean")
        print_status "Cleaning up cache and temporary files..."
        rm -rf __pycache__ .pytest_cache .ruff_cache
        rm -rf logs/*.log
        print_success "Cleanup completed"
        ;;
    
    "shell")
        print_status "Starting shell in uv environment..."
        check_uv
        uv run bash
        ;;
    
    "deps")
        print_status "Showing dependency tree..."
        check_uv
        uv tree
        ;;
    
    "update")
        print_status "Updating dependencies..."
        check_uv
        uv sync --upgrade
        print_success "Dependencies updated successfully"
        ;;
    
    "help"|"-h"|"--help")
        show_help
        ;;
    
    *)
        print_error "Unknown command: $1"
        show_help
        exit 1
        ;;
esac

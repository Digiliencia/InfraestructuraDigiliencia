# Use official dev container base image with Python 3.13
FROM mcr.microsoft.com/devcontainers/python:3.13-bookworm

# Install uv (Python package manager) from GitHub container registry
COPY --from=ghcr.io/astral-sh/uv:0.6.1 /uv /uvx /bin/

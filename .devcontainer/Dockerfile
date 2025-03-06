FROM mcr.microsoft.com/devcontainers/python:1-3.13-bullseye

# Instalar GIMP
RUN apt-get update && apt-get install -y gimp

# Instalar Python
RUN apt-get install -y python3 python3-pip

# Actualizar pip
RUN pip install --upgrade pip

#Descargar el requirements.txt
RUN pip3 install --no-cache-dir rich selenium python-dotenv loguru
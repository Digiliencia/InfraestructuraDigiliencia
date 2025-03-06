FROM mcr.microsoft.com/devcontainers/base:bullseye

# Instalar GIMP
RUN apt-get update && apt-get install -y gimp

# Instalar Python
RUN apt-get install -y python3 python3-pip

#Descargar el requirements.txt
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt
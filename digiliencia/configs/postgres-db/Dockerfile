# Oficial PostgreSQL image
FROM postgres:17

RUN apt-get update && apt-get install -y gettext

# Copy the content of the folder 'scripts' to /docker-entrypoint-initdb.d/
# The offical PostgreSQL image will execute
# any script (.sql, .sh) in this folder
# during the initialization of the database
COPY ./scripts/ /docker-entrypoint-initdb.d/

# 5432 is the default port for PostgreSQL
EXPOSE 5432
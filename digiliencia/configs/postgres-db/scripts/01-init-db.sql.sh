#!/bin/bash
set -e # Salir inmediatamente si un comando falla

echo "Processing SQL template and initializing database/users..."

# Accede a las variables de entorno necesarias.
# No necesitamos acceder a *todas* las variables aquí, solo las que envsubst usará
# en la plantilla SQL. envsubst leerá todas las variables de entorno del contenedor.

# Define las variables que envsubst debe buscar y sustituir.
# Esto es opcional si quieres que envsubst sustituya *todas* las variables de entorno
# con formato ${VAR} o $VAR, pero es más seguro ser explícito.
VARIABLES_TO_SUBSTITUTE='$APP_DB_NAME $DB_OWNER_USER $DB_OWNER_PASSWORD $APP_USER $APP_USER_PASSWORD'

# Procesa la plantilla SQL: sustituye las variables de entorno y envía la salida a psql
# ON_ERROR_STOP=1 hará que psql salga inmediatamente si encuentra un error
# --username "$POSTGRES_USER" asegura que nos conectamos como el superusuario
# --dbname "postgres" (o dejar por defecto) es seguro para crear otras DBs/usuarios
envsubst < /docker-entrypoint-initdb.d/01-init-db.sql.template | \
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "postgres"

echo "SQL template processed and executed."

# Los siguientes scripts (02 y 03) se ejecutarán automáticamente después de este
# y normalmente se ejecutarán contra la base de datos especificada en POSTGRES_DB
# (o la base de datos por defecto del usuario, 'postgres'), pero asumen
# que la DB y los usuarios ya existen y tienen permisos básicos.
# Si 02-create-schema.sql necesita conectarse específicamente a $APP_DB_NAME,
# y POSTGRES_DB no está seteado a $APP_DB_NAME en el .env,
# puede que necesites ajustar 02 o 03 para que explícitamente se conecten
# o usar la variable POSTGRES_DB en el .env.
# La forma más común es setear POSTGRES_DB=$APP_DB_NAME en el .env
# para que el entrypoint conecte los scripts .sql posteriores a esa DB.
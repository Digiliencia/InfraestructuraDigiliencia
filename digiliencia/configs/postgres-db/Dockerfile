# Usa la imagen oficial de PostgreSQL como base
FROM postgres:17

# Copia todos los archivos del directorio 'scripts' a /docker-entrypoint-initdb.d/
# Este directorio es especial: la imagen oficial de postgres ejecutará
# cualquier script (.sql, .sh) que encuentre aquí en orden alfabético
# durante la primera inicialización de la base de datos.
COPY ./scripts/ /docker-entrypoint-initdb.d/

# El puerto 5432 es el puerto por defecto de PostgreSQL.
EXPOSE 5432
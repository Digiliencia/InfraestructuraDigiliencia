# THis script set up POstgreSQL container.
docker run --name postgres \
--env-file .env \
-p 5432:5432 \
postgres
#-v postgres_data:/var/lib/postgresql/data \
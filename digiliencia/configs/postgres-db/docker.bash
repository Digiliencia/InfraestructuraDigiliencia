docker run --name postgres \
--env-file .env \
-v postgres_data:/var/lib/postgresql/data \
-p 5432:5432 \
postgres
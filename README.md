The goal of this project is to practice some Python behaviours

##To run postgres:
```
docker run --rm --name my_postgres -e POSTGRES_USER=postgres_user -e POSTGRES_PASSWORD=postgres_password -e POSTGRES_DB=postgres_db  -p 5432:5432 -d postgres
```
```
docker exec -it my_postgres psql -U postgres_user postgres_db
```
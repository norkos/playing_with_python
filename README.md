## What is this project about ?

The goal of the project was to play with few Python features

## What is used here?
- pydantic
- asyncio with REST
- asyncio with DBs

## What is on TODO list
- types

## How to run it
- to play with Postgres 
   - `docker run --rm --name my_postgres -e POSTGRES_USER=postgres_user -e POSTGRES_PASSWORD=postgres_password -e POSTGRES_DB=postgres_db  -p 5432:5432 -d postgres`
   - `docker exec -it my_postgres psql -U postgres_user postgres_db`
- for the rest just run selected `main.py`
  
## Have fun ;)

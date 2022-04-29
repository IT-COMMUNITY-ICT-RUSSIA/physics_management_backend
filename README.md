# physics_management_backend

Backend for Remote Physics Lab Management

Written with:

* Python
* FastAPI
* MongoDB

# Install 

```sh
poetry install
```

# Running server

## Dockerized (**Recommended**)

```sh
docker-compose up --build
```

## via Uvicorn

```sh
uvicorn app:api --reload
```

# Manage configuration 

Edit `.env` file according to information inside the file
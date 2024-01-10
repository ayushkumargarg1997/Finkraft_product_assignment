# Finkraft_product_assignment


# FastAPI Project

## Introduction

This is a FastAPI project that serves as a backend for [Your Project Name]. It follows modern web development practices, including RESTful APIs, authentication, and database integration.

## Features

- **FastAPI:** Utilizes the FastAPI framework for building APIs with Python 3.8+ type hints.
- **Authentication:** Implements JWT-based authentication for securing API endpoints.
- **Database Integration:** Connects to a PostgreSQL database for storing and retrieving data.
- **MongoDB Integration:** Integrates with MongoDB for specific functionalities.
- **Docker Support:** Includes Dockerfiles for containerization and docker-compose for managing dependencies.


### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/) (for running the project using Docker)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ayushkumargarg1997/Finkraft_product_assignment.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Finkraft_product_assignment
    ```


3. Create .env file in root directory with following variables:

```bash
MONGO_URL=mongodb://mongouser:mongopass@mongo:27017/
POSTGRES_USER=test_user
POSTGRES_PASSWORD=test_pass
POSTGRES_DB=test_db
jwt_secret=secret_test
jwt_algorithm=HS256
```


4. Create config.ini file inside app/db with the following variables:

```bash
[postgresql]
host = db
port = 5432
database = test_db
username = test_user
password = test_pass
```


### Running the Application


#### With Docker

```bash
docker-compose up -–build -d
```



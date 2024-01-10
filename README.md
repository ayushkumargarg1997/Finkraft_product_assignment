# Finkraft_product_assignment


# FastAPI Project

## Introduction

This is a FastAPI project which have user management and product catalog. It follows modern web development practices, including RESTful APIs, authentication, and database integration.

## Features

- **FastAPI:** Utilizes the FastAPI framework for building APIs with Python 3.8+ type hints.
- **Authentication:** Implements JWT-based authentication for securing API endpoints.
- **Database Integration:** Connects to a PostgreSQL database for storing and retrieving relational user data.
- **MongoDB Integration:** Connects with MongoDB for product catalog.
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


```bash
docker-compose up -–build -d
```

The above command will install the necessary dependencies and initialise the project with loading the sample data.

You can view the list of all the api and use it on Swagger UI by

```bash
http://localhost:8000/docs
```

or

```bash
http://127.0.0.1:8000/docs
```

<img width="1440" alt="image" src="https://github.com/ayushkumargarg1997/Finkraft_product_assignment/assets/73874155/bf5e790a-52f0-4fc7-a417-b77e2881396d">



# User Management API

This project implements a simple Flask server for managing users via a REST API. It includes the following basic CRUD operations:

- **Create a new user** (POST /users)
- **Get a list of all users** (GET /users)
- **Get details of a specific user** (GET /users/{id})
- **Update user data** (PUT /users/{id})
- **Delete a user** (DELETE /users/{id})

## Features

- **Flask** is used for creating the API.
- **SQLAlchemy** is used for database interaction (supports MySQL).
- **Docker** is used for containerizing the application and the database.
- **Testing** is integrated using `pytest`.
- **Swagger** or other documentation libraries for API auto-documentation.

## Prerequisites

Before running the application, ensure that you have the following tools installed:

- Docker
- Docker Compose

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone url_repository
   ```
2. Create a .env file in the root directory and configure your environment variables (e.g., database connection).

3.Build and start the Docker containers:
  ```bash
  docker-compose up --build
  ```
  This will build the Flask application and start the database container.

4. The Flask app will be available at http://localhost:5000

## Running Tests

To run the tests inside the Docker container, use the following command:
```bash
docker-compose exec -it pytest
```
## Conventional Commits
This project follows the Conventional Commits specification. Each commit message should include a type and a short description of the change. For example:

feat: add user creation endpoint

fix: resolve issue with user update

chore: update dependencies

## API Documentation
Swagger auto-documentation is available at the following URL after starting the application: http://localhost:5000/swagger

## Directory Structure
The project follows a Modular Architecture (or Layered Architecture) approach, where different components of the application are organized into independent modules or layers. Below is the directory structure:
```
├── app/
│   ├── controllers/
│   ├── db/
│   ├── migrations/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── tests/
│   ├── utils/
│   ├── Dockerfile
│   ├── entrypoint.sh
│   ├── requirements.txt
│   ├── config.py
│   ├── wsgi.py
├── docker-compose.yml
├── .gitignore
├── pytest.ini
└── README.md
```

### Architecture Overview

This project is built using Modular Architecture, where different components like controllers, models, services, and routes are independent modules, each responsible for a specific part of the application logic.
Alternatively, it follows a Layered Architecture approach, where the project is divided into logical layers:

Controller Layer (controllers/) - Handles incoming API requests.

Service Layer (services/) - Contains the business logic.

Data Access Layer (db/ and models/) - Responsible for interaction with the database.

Configuration Layer (config.py, Dockerfile) - Contains all the necessary configuration files for the project.


## Notes

The `entrypoint.sh` script is used to check for and apply any pending database migrations before starting the Flask app.

Ensure that you have the correct database configuration in your `.env` file.

### Potential Issue with Line Endings (CRLF) on Windows

If you are running this project on Windows, you may encounter issues with the `entrypoint.sh` script due to Windows-style line endings (`\r\n`, known as CRLF). This can cause errors like:
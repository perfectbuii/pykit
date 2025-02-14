---

| _ \ \ / / | |/ /_ _|_ _|
| _/\ V / | ' < | | | |  
 |_| |_| |_|\_\_\_\_| |_|

## Description

Pykit is a FastAPI-based application designed to manage user data with a PostgreSQL database. It includes endpoints for creating, retrieving, updating, and deleting users. The application uses SQLAlchemy for ORM and Pydantic for data validation. The project follows a clean architecture template to ensure maintainability and scalability.

## Features

- User management
- FastAPI for building APIs
- Pydantic for data validation
- PostgreSQL database integration
- USe Alembic for migrations
- SQLAlchemy for ORM

## Prerequisites

- Docker
- Docker Compose

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/perfectbuii/pykit.git
   cd pykit
   ```

2. Create a [`.env`] file in the root directory and add the following environment variables:
   ```env
   POSTGRES_USER=your_postgres_user
   POSTGRES_PASSWORD=your_postgres_password
   POSTGRES_DB=your_postgres_db
   ENV=docker
   ```

## Running the Application

1. Build and start the application using Docker Compose:

   ```sh
   docker-compose down --rmi all && docker-compose up --build --force-recreate
   ```

2. The application will be available at [`http://localhost:8000`].

## API Endpoints

- [`POST /api/user/`] - Create a new user

## Testing the API

You can test the API by navigating to [`http://localhost:8000/docs`] in your web browser. This will open the interactive API documentation provided by FastAPI, where you can run and test the API endpoints directly.

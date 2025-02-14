#!/bin/sh

# Print a message indicating that Alembic migrations are being run
echo "Running Alembic migrations..."
# Run Alembic migrations to upgrade the database schema to the latest version
poetry run alembic upgrade head

# Print a message indicating that the application is starting
echo "Starting the application..."
# Start the FastAPI application using Uvicorn, listening on all interfaces (0.0.0.0) and port 8000
poetry run uvicorn cmd.main:app --host 0.0.0.0 --port 8000
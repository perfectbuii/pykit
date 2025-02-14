# Use the official Python 3.13 slim image as the base image
FROM python:3.13-slim

# Update the package list and install necessary packages
RUN apt-get update && apt-get install -y curl build-essential libpq-dev

# Install Poetry, a dependency management tool for Python
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to the PATH environment variable
ENV PATH="/root/.local/bin:$PATH"

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the dependency files to the working directory
COPY pyproject.toml poetry.lock /app/

# Install the dependencies specified in pyproject.toml
RUN poetry install --no-root

# Copy the entire application code to the working directory
COPY . /app

# Copy the entrypoint script to the working directory and make it executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expose port 8000 to allow external access to the application
EXPOSE 8000

# Set the entrypoint to the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]
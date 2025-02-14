# Target to run the FastAPI application
run:
    # Use Poetry to run Uvicorn, specifying the application entry point and host/port configuration
    poetry run uvicorn cmd.main:app --host 0.0.0.0 --port 8000
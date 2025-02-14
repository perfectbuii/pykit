from fastapi import FastAPI
from typing import AsyncIterator
from infra.database.database_init import check_database_connection, SessionLocal
from internal.router.api_router import ApiRouter


# Function to create and configure the FastAPI application
def create_app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan_handler
    )  # Initialize FastAPI app with a lifespan handler

    db = SessionLocal()  # Create a new database session
    api_router = ApiRouter(db=db)  # Initialize API router with the database session
    app.include_router(
        api_router.get_router(), prefix="/api"
    )  # Include the API router with a prefix

    return app  # Return the configured FastAPI app


# Lifespan handler for the FastAPI application
async def lifespan_handler(app: FastAPI) -> AsyncIterator[None]:
    print("Starting app...")  # Print a message when the app starts
    check_database_connection()  # Check the database connection
    yield  # Yield control back to the application
    print("Shutting down app...")  # Print a message when the app shuts down


# Create the FastAPI app instance
app = create_app()

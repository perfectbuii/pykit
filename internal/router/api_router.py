from fastapi import APIRouter
from sqlalchemy.orm import Session
from internal.router.user import init_user_service


# Class to initialize and configure the API router
class ApiRouter:
    def __init__(self, db: Session):
        self.db = db  # Database session

    # Method to get the configured API router
    def get_router(self) -> APIRouter:
        api_router = APIRouter()  # Create a new APIRouter instance

        # Include the user service router with a prefix and tags
        api_router.include_router(
            init_user_service(self.db), prefix="/user", tags=["User"]
        )

        return api_router  # Return the configured APIRouter instance

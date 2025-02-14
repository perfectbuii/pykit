from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from internal.repository.user import SQLAlchemyUserRepository
from internal.domain.user import CreateUserRequest, CreateUserResponse
from internal.use_case.user_create import UserCreateUseCase


# Function to initialize the user service router
def init_user_service(db: Session) -> APIRouter:
    router = APIRouter()  # Create a new APIRouter instance

    user_repository = SQLAlchemyUserRepository(
        db
    )  # Initialize the user repository with the database session
    user_create_use_case = UserCreateUseCase(
        user_repository
    )  # Initialize the use case for creating a user

    # Endpoint to create a new user
    @router.post("/", response_model=CreateUserResponse)
    def create_user(user: CreateUserRequest):
        created_user = user_create_use_case.execute(
            name=user.name, email=user.email
        )  # Execute the use case to create a user

        if not created_user:
            raise HTTPException(
                status_code=400, detail="Email already in use"
            )  # Raise an exception if the email is already in use

        return CreateUserResponse(id=created_user.id, name=created_user.name, email=created_user.email)


    return router  # Return the configured APIRouter instance

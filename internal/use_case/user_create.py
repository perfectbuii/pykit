from internal.repository.user import UserRepository
from internal.domain.user import User as DomainUser


# Use case class for creating a user
class UserCreateUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = (
            user_repository  # User repository for database operations
        )

    # Execute the use case to create a new user
    def execute(self, name: str, email: str) -> DomainUser:
        existing_user = self.user_repository.find_by_email(
            email
        )  # Check if a user with the given email already exists
        if existing_user:
            return None  # Return None if the email is already in use

        new_user = self.user_repository.create(
            name=name, email=email
        )  # Create a new user
        return new_user  # Return the newly created user

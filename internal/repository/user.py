from typing import List, Optional
from internal.domain.user import User as DomainUser
from infra.database.schema.user import User as SQLAlchemyUser
from sqlalchemy.orm import Session


# Abstract repository class for User operations
class UserRepository:
    def create(self, name: str, email: str) -> DomainUser:
        raise NotImplementedError

    def get_by_id(self, user_id: int) -> Optional[DomainUser]:
        raise NotImplementedError

    def get_all(self, skip: int = 0, limit: int = 10) -> List[DomainUser]:
        raise NotImplementedError

    def find_by_email(self, email: str):
        raise NotImplementedError


# SQLAlchemy implementation of the UserRepository
class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, db: Session):
        self.db = db  # Database session

    # Create a new user in the database
    def create(self, name: str, email: str) -> DomainUser:
        db_user = SQLAlchemyUser(
            name=name, email=email
        )  # Create a new SQLAlchemy user instance
        self.db.add(db_user)  # Add the user to the session
        self.db.commit()  # Commit the transaction
        self.db.refresh(db_user)  # Refresh the instance to get the generated ID
        return db_user.to_domain()  # Convert to domain model and return

    # Get a user by ID from the database
    def get_by_id(self, id: int) -> Optional[DomainUser]:
        db_user = (
            self.db.query(SQLAlchemyUser).filter(SQLAlchemyUser.id == id).first()
        )  # Query the user by ID
        return (
            db_user.to_domain() if db_user else None
        )  # Convert to domain model if found, else return None

    # Find a user by email in the database
    def find_by_email(self, email: str):
        return (
            self.db.query(SQLAlchemyUser).filter(SQLAlchemyUser.email == email).first()
        )  # Query the user by email

    # Get all users with pagination
    def get_all(self, skip: int = 0, limit: int = 10) -> List[DomainUser]:
        db_users = (
            self.db.query(SQLAlchemyUser).offset(skip).limit(limit).all()
        )  # Query users with offset and limit
        return [
            user.to_domain() for user in db_users
        ]  # Convert to domain models and return as a list

    # Update an existing user in the database
    def update(self, user: DomainUser) -> Optional[DomainUser]:
        db_user = (
            self.db.query(SQLAlchemyUser).filter(SQLAlchemyUser.id == user.id).first()
        )  # Query the user by ID
        if db_user:
            db_user.name = user.name  # Update the name
            db_user.email = user.email  # Update the email
            self.db.commit()  # Commit the transaction
            self.db.refresh(db_user)  # Refresh the instance
        return (
            db_user.to_domain() if db_user else None
        )  # Convert to domain model if found, else return None

    # Delete a user by ID from the database
    def delete(self, user_id: int) -> None:
        db_user = (
            self.db.query(SQLAlchemyUser).filter(SQLAlchemyUser.id == user_id).first()
        )  # Query the user by ID
        if db_user:
            self.db.delete(db_user)  # Delete the user from the session
            self.db.commit()  # Commit the transaction

from sqlalchemy import Column, Integer, String
from internal.domain.user import User as DomainUser
from infra.database.database_init import Base  

# SQLAlchemy model for the User table
class User(Base):
    __tablename__ = "users"  # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    name = Column(String, index=True)  # Name column with an index
    email = Column(String, unique=True, index=True)  # Email column with a unique constraint and an index

    # Convert the SQLAlchemy User model to a domain User model
    def to_domain(self) -> DomainUser:
        return DomainUser(id=self.id, name=self.name, email=self.email)

    # Create an instance of the SQLAlchemy User model from a domain User model
    @classmethod
    def from_domain(cls, user: DomainUser):
        return cls(id=user.id, name=user.name, email=user.email)
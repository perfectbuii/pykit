from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Determine the database URL based on the environment
if os.getenv("ENV") == "local":
    # Local environment database URL
    SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
else:
    # Docker environment database URL
    SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@db/postgres"

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative class definitions
Base = declarative_base()


# Function to check the database connection
def check_database_connection():
    try:
        # Attempt to connect to the database and execute a simple query
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database connected successfully.")
    except SQLAlchemyError as e:
        # Print an error message if the connection fails
        print(f"Error connecting to the database: {e}")

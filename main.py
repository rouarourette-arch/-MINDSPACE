
# Import all models and configure their relationships
from backend.models.relationships import *

# Import database engine
from backend.database.connection import engine


def main():
    try:
        with engine.connect() as connection:
            print("Database connection successful!")

    except Exception as error:
        print("Database connection failed:", error)


if __name__ == "__main__":
    main()

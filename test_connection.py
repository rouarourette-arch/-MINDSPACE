from backend.database.connection import engine
try:
    with engine.connect() as connection:
        print("Database connection successful!")
        print("Connected to:", engine.url.database)

except Exception as error:
    print("Database connection failed!")
    print(error)

finally:
    engine.dispose()
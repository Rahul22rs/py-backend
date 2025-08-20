from db.config import execute_ddl, get_engine

if __name__ == "__main__":
    engine = get_engine()
    execute_ddl(engine=engine)
    print('--- Success')



# from app.db.config import get_engine
# from app.models.base import Base

# print("Creating tables...")
# engine = get_engine()
# Base.metadata.create_all(bind=engine)
# print("✅ Success")

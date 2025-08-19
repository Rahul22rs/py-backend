from db.config import execute_ddl, get_engine

if __name__ == "__main__":
    engine = get_engine()
    execute_ddl(engine=engine)
    print('--- Success')

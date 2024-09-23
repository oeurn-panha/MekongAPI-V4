from sqlalchemy import create_engine  #sqlalchemy is ORM
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL_DATABASE = "postgresql://username:password@localhost:5432/db_name"
URL_DATABASE = "postgresql://panha:panha123@127.0.0.1:5432/mekong"

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

    # db.add(db_data)
    # db.commit()
    # db.refresh(db_data)
from typing import Annotated

from fastapi import Depends
from sqlalchemy import engine, create_engine
from sqlalchemy.orm import (
    sessionmaker,
    Session,
    declarative_base,
)


SQL_ALCHEMY_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(SQL_ALCHEMY_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

Base = declarative_base()

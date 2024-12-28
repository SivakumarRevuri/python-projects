from sqlalchemy import Column, Integer, String, Boolean
from main import Base


class User(Base):

    __tablename__ = "users"

    id: int = Column(
        "ID", Integer, primary_key=True, index=True, autoincrement=True
    )
    username: str = Column("USER_NAME", String, unique=True, nullable=False)
    password: str = Column("PASSWORD", String, nullable=False)
    email: str = Column("EMAIL", String, nullable=False, unique=True)
    is_activate: bool = Column("IS_ACTIVATE", Boolean, nullable=False)
    role: str = Column("ROLE", String, nullable=True)

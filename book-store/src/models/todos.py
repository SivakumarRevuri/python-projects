from main import Base

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Todos(Base):

    __tablename__ = "todos"

    id: int = Column("ID", Integer, autoincrement=True, primary_key=True, index=True)
    title: str = Column("TITLE", String, nullable=False)
    description: str = Column("DESCRIPTION", String)
    priority: int = Column("PRIORITY", Integer)
    complete: bool = Column("COMPLETE", Boolean)

    owner_id: int = Column("OWNER_ID", ForeignKey("users.id"))

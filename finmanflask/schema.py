from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.orm import Mapped


class Base(DeclarativeBase):
    pass

class User(Base):
    # since 'user' is a reserved keyword, the name is as such:
    __tablename__ = 'finmanuser'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(255)) # I am not sure about the character limit here
    email: Mapped[str] = mapped_column(String(100))
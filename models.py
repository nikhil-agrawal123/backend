from .database import Base
from sqlalchemy import Column, Integer, String,ForeignKey,JSON
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True,)
    password = Column(String)

    items = relationship("Content", back_populates="owner")

class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(JSON)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")
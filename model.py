from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Node(Base):
    __tablename__ = "Node"

    id = Column(Integer, primary_key=True, index=True)
    desc = Column(String)
    number = Column(Integer)
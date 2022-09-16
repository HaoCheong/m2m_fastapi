from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

# Node Table
class Node(Base):
    __tablename__ = "Node"

    id = Column(String, primary_key=True, index=True)
    desc = Column(String)
    number = Column(Integer)
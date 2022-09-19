from turtle import back
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class NodeAssociation(Base):
    __tablename__ = 'node_association'
    node_parent_id = Column(Integer, ForeignKey('Node.id'), primary_key=True)
    node_child_id =Column(Integer, ForeignKey('Node.id'), primary_key=True)
    extra_num = Column(Integer)
    child = relationship('Node', back_populates="parent_nodes")
    parent = relationship('Node', back_populates="child_nodes")

# Node Table
class Node(Base):
    __tablename__ = "Node"

    id = Column(String, primary_key=True, index=True)
    desc = Column(String)
    number = Column(Integer)

    child_nodes = relationship('NodeAssociation', back_populates='parent')
    parent_nodes = relationship('NodeAssociation', back_populates='child')
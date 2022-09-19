from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class NodeAssociation(Base):
    __tablename__ = 'node_association'
    node_parent_id = Column(Integer, ForeignKey('Node.id'), primary_key=True)
    node_child_id =Column(Integer, ForeignKey('Node.id'), primary_key=True)

# Node Table
class Node(Base):
    __tablename__ = "Node"

    id = Column(String, primary_key=True, index=True)
    desc = Column(String)
    number = Column(Integer)

    child_nodes = relationship('Node',
                                 secondary='node_association',
                                 primaryjoin=id==NodeAssociation.node_parent_id,
                                 secondaryjoin=id==NodeAssociation.node_child_id,
                                 backref='childs')
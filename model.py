from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from database import Base

node_association = Table('node_association', Base.metadata,
    Column('parent_id', ForeignKey('Node.id'), primary_key=True),
    Column('child_id', ForeignKey('Node.id'), primary_key=True)
)

# Node Table
class Node(Base):
    __tablename__ = "Node"

    id = Column(String, primary_key=True, index=True)
    desc = Column(String)
    number = Column(Integer)

    # sub_nodes = relationship('Node', secondary='node_association', back_populates='Node')
    child_nodes = relationship('Node',
        secondary=node_association,
        primaryjoin=id==node_association.c.parent_id,
        secondaryjoin=id==node_association.c.child_id,
        backref='children'
    )
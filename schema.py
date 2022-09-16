from typing import List, Union, Optional
from pydantic import BaseModel

# Base Node Schema
class NodeBase(BaseModel):
  desc: str
  number: int

# Read Node Schema, version A
class NodeRead_A(NodeBase):
  id: str

  class Config:
    orm_mode = True

# Read Node Schema, version B
class NodeRead_B(NodeBase):
  id: str

  class Config:
    orm_mode = True

# Create Node Schema
class NodeCreate(NodeBase):
  id: str

# Update Node Schema
class NodeUpdate(NodeBase):
  id: Optional[str]
  desc: Optional[str]
  number: Optional[int]
  


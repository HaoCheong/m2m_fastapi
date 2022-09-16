from typing import List, Union, Optional

from pydantic import BaseModel

class NodeBase(BaseModel):
  desc: str
  number: int

class NodeRead_A(NodeBase):
  id: str

  class Config:
    orm_mode = True

class NodeRead_B(NodeBase):
  id: str

  class Config:
    orm_mode = True

class NodeCreate(NodeBase):
  id: str

class NodeUpdate(NodeBase):
  id: Optional[str]
  desc: Optional[str]
  number: Optional[int]
  


from typing import List, Union, Optional

from pydantic import BaseModel

class NodeBase(BaseModel):
  desc: str
  number: int

class NodeRead_A(NodeBase):
  id: str

class NodeRead_B(NodeBase):
  id: str

class NodeCreate(NodeBase):
  id: str

class NodeUpdate(NodeBase):
  desc: Optional[str]
  number: Optional[int]
  id: Optional[str]


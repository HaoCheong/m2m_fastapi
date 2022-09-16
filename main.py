from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, model, schema
from database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get all nodes, respond with list of Node Read Version A
@app.get("/nodes/", response_model=List[schema.NodeRead_A])
def get_all_nodes(limit: int = 10, db: Session = Depends(get_db)):
  nodes = crud.get_all_nodes(db, limit=limit)
  return nodes

# Get a node given a valid node id, respond with Node Read Version B
@app.get("/nodes/{node_id}", response_model=schema.NodeRead_B)
def get_node_by_node_id(node_id: str, db: Session = Depends(get_db)):
  db_node = crud.get_node_by_node_id(db, node_id = node_id)
  if db_node is None:
    raise HTTPException(status_code=404, detail="Node not found")

  return db_node

# Create a new node, respond with Node Read Version B
@app.post("/nodes/", response_model=schema.NodeRead_B)
def create_node(node: schema.NodeCreate, db: Session = Depends(get_db)):
  return crud.create_node(db, node=node)

# Delete node given a valid node id, respond with Success Dict
@app.delete("/nodes/{node_id}")
def delete_node(node_id: str, db: Session = Depends(get_db)):
  db_node = crud.get_node_by_node_id(db, node_id = node_id)
  if db_node is None:
    raise HTTPException(status_code=404, detail="Node not found")

  return crud.delete_node(db, node_id=node_id)

# Update/patch node given a valid node id, respond with Success Dict
@app.patch("/nodes/{node_id}")
def update_node_by_node_id(node_id: str, new_node: schema.NodeUpdate, db: Session = Depends(get_db)):
  db_node = crud.get_node_by_node_id(db, node_id = node_id)
  if db_node is None:
    raise HTTPException(status_code=404, detail="Node not found")

  return crud.update_node_by_node_id(db, node_id=node_id, new_node=new_node)

# Assign Child Part to Parent Part
@app.post("/nodes/{parent_id}/{child_id}")
def add_child_node_to_parent_node(parent_id: str, child_id: str, db: Session = Depends(get_db)):
  parent_node = crud.get_node_by_node_id(db, node_id = parent_id)
  child_node = crud.get_node_by_node_id(db, node_id = child_id)

  if not parent_node:
    raise HTTPException(status_code=404, detail="Parent node not found")

  if not child_node:
    raise HTTPException(status_code=404, detail="Child node not found")

  return crud.add_child_node_to_parent_node(db, child_id=child_id, parent_id=parent_id)
  
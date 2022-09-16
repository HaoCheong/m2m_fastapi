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

@app.get("/nodes/", response_model=List[schema.NodeRead_A])
def get_all_nodes(limit: int = 10, db: Session = Depends(get_db)):
  nodes = crud.get_all_nodes(db, limit=limit)
  return nodes

@app.get("/nodes/{node_id}", response_model=schema.NodeRead_B)
def get_node_by_node_id(node_id: str, db: Session = Depends(get_db)):
  db_node = crud.get_node_by_node_id(db, node_id = node_id)
  if db_node is None:
    raise HTTPException(status_code=404, detail="Node not found")

  return db_node

@app.post("/nodes/", response_model=schema.NodeRead_B)
def create_node(node: schema.NodeCreate, db: Session = Depends(get_db)):
  return crud.create_node(db, node=node)

@app.delete("/nodes/{node_id}")
def delete_node(node_id: str, db: Session = Depends(get_db)):
  db_node = crud.get_node_by_node_id(db, node_id = node_id)
  if db_node is None:
    raise HTTPException(status_code=404, detail="Node not found")

  return crud.delete_node(db, node_id=node_id)
  
@app.patch("/nodes/{node_id}")
def update_node_by_node_id(node_id: str, new_node: schema.NodeUpdate, db: Session = Depends(get_db)):
  db_node = crud.get_node_by_node_id(db, node_id = node_id)
  if db_node is None:
    raise HTTPException(status_code=404, detail="Node not found")

  return crud.update_node_by_node_id(db, node_id=node_id, new_node=new_node)

  
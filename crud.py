from sqlalchemy.orm import Session

from . import model, schema

def get_all_nodes(db: Session, limit: int = 10):
  return db.query(model.Node).limit(limit).all()

def get_node_by_node_id(db: Session, node_id: str):
  return db.query(model.Node).filter(model.Node.id == node_id).first()

def create_node(db: Session, node: schema.NodeCreate):
  db_node = model.Node(
    desc=node.desc,
    number=node.number,
    id=node.id
  )

  db.add(db_node)
  db.commit()
  db.refresh()

  return db_node

def delete_node(db: Session, node_id: str):
  db_node = db.query(model.Node).filter(model.Node.id == node_id).first()
  if not db_node:
    return None

  db.delete(db_node)
  db.commit()
  return {"Success": True}

def update_node_by_node_id(db: Session, node_id: str, new_node: schema.NodeUpdate):
  db_node = db.query(model.Node).filter(model.Node.id == node_id).first()
  if not db_node:
    return None

  update_data = new_node.dict(exclude_unset=True)
  
  for key, value in update_data.items():
    setattr(db_node, key, value)

  db.add(db_node)
  db.commit()
  db.refresh(db_node)


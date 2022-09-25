from sqlalchemy.orm import Session
import model, schema
from fastapi.encoders import jsonable_encoder

# Get all the nodes, limited to 10
def get_all_nodes(db: Session, limit: int = 10):
  return db.query(model.Node).limit(limit).all()

# Get all node by a given node id
def get_node_by_node_id(db: Session, node_id: str):
  return db.query(model.Node).filter(model.Node.id == node_id).first()

# Create a node in the schema NodeCreate
def create_node(db: Session, node: schema.NodeCreate):
  db_node = model.Node(
    desc=node.desc,
    number=node.number,
    id=node.id
  )

  db.add(db_node)
  db.commit()
  db.refresh(db_node)

  return db_node

# Delete a node given a valid node_id
def delete_node(db: Session, node_id: str):
  db_node = db.query(model.Node).filter(model.Node.id == node_id).first()
  if not db_node:
    return None

  db.delete(db_node)
  db.commit()

  return {"Success": True}

# Update a node selectively given a valid node_id
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

  return {"Success": True}

def assign_child_to_parent(db: Session, child_id: str, parent_id: str, extra_num: int):
  db_parent_node = db.query(model.Node).filter(model.Node.id == parent_id).first()
  db_child_node = db.query(model.Node).filter(model.Node.id == child_id).first()

  db_parent_node.child_nodes.append(db_child_node)

  db.add(db_parent_node)
  db.commit()

  db_row = db.query(model.NodeAssociation).filter(model.NodeAssociation.node_parent_id == parent_id).filter(model.NodeAssociation.node_child_id == child_id).first()
  db_row.extra_num = extra_num

  db.add(db_row)
  db.commit()
  db.refresh(db_row)

  return {"Success": True}
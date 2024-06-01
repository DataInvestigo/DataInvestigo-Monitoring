from sqlalchemy.orm import Session
from app import models, schemas

def get_resource_utilization(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ResourceUtilization).offset(skip).limit(limit).all()

def create_resource_utilization(db: Session, resource: schemas.ResourceUtilizationCreate):
    db_resource = models.ResourceUtilization(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

# Define other CRUD operations similarly...

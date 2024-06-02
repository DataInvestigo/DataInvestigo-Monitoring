from sqlalchemy.orm import Session
from app import models, schemas

# Resource Utilization
def get_resource_utilization(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ResourceUtilization).offset(skip).limit(limit).all()

def create_resource_utilization(db: Session, resource: schemas.ResourceUtilizationCreate):
    db_resource = models.ResourceUtilization(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

# System Health
def get_system_health(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.SystemHealth).offset(skip).limit(limit).all()

def create_system_health(db: Session, health: schemas.SystemHealthCreate):
    db_health = models.SystemHealth(**health.dict())
    db.add(db_health)
    db.commit()
    db.refresh(db_health)
    return db_health

# Security
def get_security(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Security).offset(skip).limit(limit).all()

def create_security(db: Session, security: schemas.SecurityCreate):
    db_security = models.Security(**security.dict())
    db.add(db_security)
    db.commit()
    db.refresh(db_security)
    return db_security

# Performance Metrics
def get_performance_metrics(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.PerformanceMetrics).offset(skip).limit(limit).all()

def create_performance_metrics(db: Session, metrics: schemas.PerformanceMetricsCreate):
    db_metrics = models.PerformanceMetrics(**metrics.dict())
    db.add(db_metrics)
    db.commit()
    db.refresh(db_metrics)
    return db_metrics

# Backup
def get_backup(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Backup).offset(skip).limit(limit).all()

def create_backup(db: Session, backup: schemas.BackupCreate):
    db_backup = models.Backup(**backup.dict())
    db.add(db_backup)
    db.commit()
    db.refresh(db_backup)
    return db_backup

# Logs
def get_logs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Logs).offset(skip).limit(limit).all()

def create_logs(db: Session, log: schemas.LogsCreate):
    db_log = models.Logs(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

# Management
def get_management(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Management).offset(skip).limit(limit).all()

def create_management(db: Session, management: schemas.ManagementCreate):
    db_management = models.Management(**management.dict())
    db.add(db_management)
    db.commit()
    db.refresh(db_management)
    return db_management

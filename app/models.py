from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from .database import Base
from datetime import datetime

class ResourceUtilization(Base):
    __tablename__ = "resource_utilization"
    id = Column(Integer, primary_key=True, index=True)
    cpu_usage = Column(Float)
    memory_usage = Column(Float)
    disk_io = Column(Float)
    network_bandwidth = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class SystemHealth(Base):
    __tablename__ = "system_health"
    id = Column(Integer, primary_key=True, index=True)
    uptime = Column(String)
    load_average = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Security(Base):
    __tablename__ = "security"
    id = Column(Integer, primary_key=True, index=True)
    failed_login_attempts = Column(Integer)
    unauthorized_access_attempts = Column(Integer)
    ids_alerts = Column(Integer)
    security_patch_status = Column(String)
    user_activity_auditing = Column(String)
    database_access_control_violations = Column(Integer)
    compliance_status = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class PerformanceMetrics(Base):
    __tablename__ = "performance_metrics"
    id = Column(Integer, primary_key=True, index=True)
    response_time = Column(Float)
    latency = Column(Float)
    throughput = Column(Float)
    error_rate = Column(Float)
    long_running_queries = Column(Integer)
    query_execution_time = Column(Float)
    query_cache_hit_ratio = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Backup(Base):
    __tablename__ = "backup"
    id = Column(Integer, primary_key=True, index=True)
    backup_status = Column(String)
    backup_duration = Column(Float)
    backup_size = Column(Float)
    backup_schedule = Column(String)
    point_in_time_recovery_capability = Column(Boolean)
    backup_storage_utilization = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Logs(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    log_type = Column(String)
    log_message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Management(Base):
    __tablename__ = "management"
    id = Column(Integer, primary_key=True, index=True)
    database_version = Column(String)
    patch_applied = Column(Boolean)
    patch_version = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

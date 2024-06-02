from pydantic import BaseModel
from datetime import datetime

# Resource Utilization
class ResourceUtilizationBase(BaseModel):
    cpu_usage: float
    memory_usage: float
    disk_io: float
    network_bandwidth: float

class ResourceUtilizationCreate(ResourceUtilizationBase):
    pass

class ResourceUtilization(ResourceUtilizationBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

# System Health
class SystemHealthBase(BaseModel):
    uptime: str
    load_average: float

class SystemHealthCreate(SystemHealthBase):
    pass

class SystemHealth(SystemHealthBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

# Security
class SecurityBase(BaseModel):
    failed_login_attempts: int
    unauthorized_access_attempts: int
    ids_alerts: int
    security_patch_status: str
    user_activity_auditing: str
    database_access_control_violations: int
    compliance_status: str

class SecurityCreate(SecurityBase):
    pass

class Security(SecurityBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

# Performance Metrics
class PerformanceMetricsBase(BaseModel):
    response_time: float
    latency: float
    throughput: float
    error_rate: float
    long_running_queries: int
    query_execution_time: float
    query_cache_hit_ratio: float

class PerformanceMetricsCreate(PerformanceMetricsBase):
    pass

class PerformanceMetrics(PerformanceMetricsBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

# Backup
class BackupBase(BaseModel):
    backup_status: str
    backup_duration: float
    backup_size: float
    backup_schedule: str
    point_in_time_recovery_capability: bool
    backup_storage_utilization: float

class BackupCreate(BackupBase):
    pass

class Backup(BackupBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

# Logs
class LogsBase(BaseModel):
    log_type: str
    log_message: str

class LogsCreate(LogsBase):
    pass

class Logs(LogsBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

# Management
class ManagementBase(BaseModel):
    database_version: str
    patch_applied: bool
    patch_version: str

class ManagementCreate(ManagementBase):
    pass

class Management(ManagementBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

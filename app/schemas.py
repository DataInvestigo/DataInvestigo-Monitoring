from pydantic import BaseModel
from datetime import datetime

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

# Define other schemas similarly...

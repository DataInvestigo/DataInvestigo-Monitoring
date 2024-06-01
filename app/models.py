from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base

class ResourceUtilization(Base):
    __tablename__ = "resource_utilization"
    id = Column(Integer, primary_key=True, index=True)
    cpu_usage = Column(Float)
    memory_usage = Column(Float)
    disk_io = Column(Float)
    network_bandwidth = Column(Float)
    timestamp = Column(DateTime)

# Define other models similarly...

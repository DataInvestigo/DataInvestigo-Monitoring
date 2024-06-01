import psutil
from datetime import datetime
from app import crud, schemas
from sqlalchemy.orm import Session

def collect_resource_utilization(db: Session):
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    disk_io = psutil.disk_io_counters().read_bytes + psutil.disk_io_counters().write_bytes
    network_bandwidth = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

    resource = schemas.ResourceUtilizationCreate(
        cpu_usage=cpu_usage,
        memory_usage=memory_usage,
        disk_io=disk_io,
        network_bandwidth=network_bandwidth
    )
    crud.create_resource_utilization(db=db, resource=resource)

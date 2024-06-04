from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from app.monitoring.resource_utilization import collect_resource_utilization
import threading
import time
import psutil

router = APIRouter()


# Global flag to control monitoring
is_monitoring = False
monitoring_thread = None

def monitoring_task(db_session_maker):
    global is_monitoring
    while is_monitoring:
        with db_session_maker() as db:
            try:
                collect_resource_utilization(db)
            except Exception as e:
                # Log the error or handle it as needed
                print(f"Error during resource collection: {e}")
            finally:
                db.close()
        time.sleep(3)

def start_monitoring_task(db_session_maker):
    global is_monitoring, monitoring_thread
    if not is_monitoring:
        is_monitoring = True
        monitoring_thread = threading.Thread(target=monitoring_task, args=(db_session_maker,))
        monitoring_thread.start()
        return {"status": "Monitoring started"}
    else:
        raise HTTPException(status_code=400, detail="Monitoring is already running")

def stop_monitoring_task():
    global is_monitoring, monitoring_thread
    if is_monitoring:
        is_monitoring = False
        monitoring_thread.join()
        monitoring_thread = None
        return {"status": "Monitoring stopped"}
    else:
        raise HTTPException(status_code=400, detail="Monitoring is not running")

@router.post("/start-monitoring")
def start_monitoring(db: Session = Depends(get_db)):
    return start_monitoring_task(get_db)

@router.post("/stop-monitoring")
def stop_monitoring():
    return stop_monitoring_task()

@router.post("/", response_model=schemas.ResourceUtilization)
def create_resource_utilization(db: Session = Depends(get_db)):
    try:
        resource = collect_resource_utilization(db)
        return resource
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=list[schemas.ResourceUtilization])
def read_resource_utilization(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    resources = crud.get_resource_utilization(db, skip=skip, limit=limit)
    return resources

@router.get("/current", response_model=schemas.ResourceUtilization)
def get_current_resource_utilization():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_io = psutil.disk_io_counters()
        net_io = psutil.net_io_counters()

        resource_data = schemas.ResourceUtilizationCreate(
            cpu_usage=cpu_usage,
            memory_usage=memory_info.percent,
            disk_io=disk_io.read_bytes + disk_io.write_bytes,
            network_bandwidth=net_io.bytes_sent + net_io.bytes_recv
        )

        return resource_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
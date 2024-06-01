from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db
import psutil
from datetime import datetime

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.post("/", response_model=schemas.ResourceUtilization)
def create_resource_utilization(resource: schemas.ResourceUtilizationCreate, db: Session = Depends(get_db)):
    return crud.create_resource_utilization(db=db, resource=resource)

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

@router.get("/view", response_class=HTMLResponse)
def view_resource_utilization(request: Request, db: Session = Depends(get_db)):
    try:
        resources = crud.get_resource_utilization(db, skip=0, limit=10)
        return templates.TemplateResponse("resource_utilization.html", {"request": request, "resources": resources})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

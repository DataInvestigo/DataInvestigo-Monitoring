from fastapi import APIRouter
from app.api.endpoints import resource_utilization, system_health, security, performance_metrics, backup, logs, management

api_router = APIRouter()
api_router.include_router(resource_utilization.router, prefix="/resource-utilization", tags=["resource-utilization"])
api_router.include_router(system_health.router, prefix="/system-health", tags=["system-health"])
api_router.include_router(security.router, prefix="/security", tags=["security"])
api_router.include_router(performance_metrics.router, prefix="/performance-metrics", tags=["performance-metrics"])
api_router.include_router(backup.router, prefix="/backup", tags=["backup"])
api_router.include_router(logs.router, prefix="/logs", tags=["logs"])
api_router.include_router(management.router, prefix="/management", tags=["management"])

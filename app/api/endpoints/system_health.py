from fastapi import APIRouter, HTTPException
import os
import subprocess

router = APIRouter()

@router.get("/uptime")
def get_server_uptime():
    try:
        uptime = subprocess.check_output(["uptime"]).decode("utf-8").strip()
        return {"uptime": uptime}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/load")
def get_load_average():
    try:
        if os.path.exists("/proc/loadavg"):
            with open("/proc/loadavg", "r") as file:
                load_avg = file.read().strip()
            return {"load_average": load_avg}
        else:
            raise HTTPException(status_code=500, detail="/proc/loadavg file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

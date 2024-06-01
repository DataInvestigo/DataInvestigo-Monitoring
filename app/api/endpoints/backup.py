from fastapi import APIRouter, HTTPException
import os
import subprocess
from datetime import datetime

router = APIRouter()

backup_directory = "/path/to/backup"

@router.get("/status")
def get_backup_status():
    try:
        backup_log = os.path.join(backup_directory, "backup.log")
        if os.path.exists(backup_log):
            with open(backup_log, "r") as file:
                logs = file.readlines()
            last_backup_status = logs[-1] if logs else "No backup logs found."
            return {"last_backup_status": last_backup_status}
        else:
            raise HTTPException(status_code=500, detail="Backup log file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/duration")
def get_backup_duration():
    try:
        start_time = datetime.now()
        # Simulate backup operation
        subprocess.run(["tar", "-czf", os.path.join(backup_directory, "backup.tar.gz"), "/path/to/data"])
        end_time = datetime.now()
        duration = end_time - start_time
        return {"backup_duration": duration.total_seconds()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/size")
def get_backup_size():
    try:
        backup_file = os.path.join(backup_directory, "backup.tar.gz")
        if os.path.exists(backup_file):
            size = os.path.getsize(backup_file)
            return {"backup_size": size}
        else:
            raise HTTPException(status_code=500, detail="Backup file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/schedule")
def get_backup_schedule():
    try:
        # Assuming a cron job is set for backups
        cron_jobs = subprocess.check_output(["crontab", "-l"]).decode("utf-8")
        backup_jobs = [job for job in cron_jobs.split('\n') if "backup" in job]
        return {"backup_schedule": backup_jobs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/point-in-time-recovery")
def get_point_in_time_recovery(timestamp: str):
    try:
        # Assuming a restore script is available
        restore_command = f"/path/to/restore_script.sh {timestamp}"
        subprocess.run(restore_command, shell=True)
        return {"status": "Recovery initiated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/storage-utilization")
def get_storage_utilization():
    try:
        df_output = subprocess.check_output(["df", "-h", backup_directory]).decode("utf-8")
        return {"storage_utilization": df_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

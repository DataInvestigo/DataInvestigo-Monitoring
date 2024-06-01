from fastapi import APIRouter, HTTPException
import os
import subprocess

router = APIRouter()

@router.get("/failed-login-attempts")
def get_failed_login_attempts():
    try:
        log_file = "/var/log/auth.log"
        if os.path.exists(log_file):
            with open(log_file, "r") as file:
                logs = file.readlines()
            failed_attempts = [line for line in logs if "Failed password" in line]
            return {"failed_login_attempts": failed_attempts}
        else:
            raise HTTPException(status_code=500, detail=f"{log_file} file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/unauthorized-access-attempts")
def get_unauthorized_access_attempts():
    try:
        log_file = "/var/log/auth.log"
        if os.path.exists(log_file):
            with open(log_file, "r") as file:
                logs = file.readlines()
            unauthorized_attempts = [line for line in logs if "authentication failure" in line]
            return {"unauthorized_access_attempts": unauthorized_attempts}
        else:
            raise HTTPException(status_code=500, detail=f"{log_file} file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/ids-alerts")
def get_ids_alerts():
    try:
        log_file = "/var/log/snort/alert"  # Assuming Snort IDS
        if os.path.exists(log_file):
            with open(log_file, "r") as file:
                alerts = file.readlines()
            return {"ids_alerts": alerts}
        else:
            raise HTTPException(status_code=500, detail=f"{log_file} file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/security-patch-status")
def get_security_patch_status():
    try:
        patches = subprocess.check_output(["apt", "list", "--upgradable"]).decode("utf-8").strip()
        return {"security_patch_status": patches}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/user-activity-auditing")
def get_user_activity_auditing():
    try:
        log_file = "/var/log/audit/audit.log"
        if os.path.exists(log_file):
            with open(log_file, "r") as file:
                logs = file.readlines()
            return {"user_activity_auditing": logs}
        else:
            raise HTTPException(status_code=500, detail=f"{log_file} file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

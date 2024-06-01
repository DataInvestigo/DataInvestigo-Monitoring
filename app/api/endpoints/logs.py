from fastapi import APIRouter, HTTPException
import os
import subprocess
import psycopg2
from psycopg2 import sql
from psycopg2.extras import DictCursor

router = APIRouter()

# Utility function to connect to the database
def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST"),
            port=os.getenv("DATABASE_PORT")
        )
        return conn
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/system-logs")
def get_system_logs():
    try:
        log_file = "/var/log/syslog"
        if os.path.exists(log_file):
            with open(log_file, "r") as file:
                logs = file.readlines()
            return {"system_logs": logs}
        else:
            raise HTTPException(status_code=500, detail=f"{log_file} file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/application-logs")
def get_application_logs():
    try:
        log_file = "/var/log/myapp/application.log"
        if os.path.exists(log_file):
            with open(log_file, "r") as file:
                logs = file.readlines()
            return {"application_logs": logs}
        else:
            raise HTTPException(status_code=500, detail=f"{log_file} file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/windows-event-logs")
def get_windows_event_logs():
    try:
        import win32evtlog
        server = 'localhost'  # name of the target computer to get event logs
        logtype = 'System'  # 'Application' or 'Security' or 'System'
        hand = win32evtlog.OpenEventLog(server, logtype)
        flags = win32evtlog.EVENTLOG_FORWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        total = win32evtlog.GetNumberOfEventLogRecords(hand)
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        event_list = []
        for event in events:
            event_list.append({
                "EventCategory": event.EventCategory,
                "TimeGenerated": event.TimeGenerated.Format(),
                "SourceName": event.SourceName,
                "EventID": event.EventID,
                "EventType": event.EventType,
                "EventData": event.StringInserts
            })
        return {"windows_event_logs": event_list}
    except ImportError:
        raise HTTPException(status_code=500, detail="pywin32 library not installed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/database-logs")
def get_database_logs():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=DictCursor)
        cursor.execute("SELECT * FROM pg_log WHERE log_time > NOW() - INTERVAL '1 day';")
        db_logs = cursor.fetchall()
        conn.close()
        return {"database_logs": db_logs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

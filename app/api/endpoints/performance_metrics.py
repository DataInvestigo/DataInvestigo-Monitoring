from fastapi import APIRouter, HTTPException
import requests
import time
import subprocess
import os
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

@router.get("/response-time")
def measure_response_time(url: str):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        response_time = end_time - start_time
        return {"response_time": response_time, "status_code": response.status_code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/latency")
def measure_latency(host: str):
    try:
        output = subprocess.check_output(["ping", "-c", "4", host]).decode("utf-8")
        latency = output.split('\n')[-2].split('/')[4]
        return {"latency": latency}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/throughput")
def measure_throughput():
    try:
        request_count = 0
        start_time = time.time()
        while time.time() - start_time < 60:
            requests.get("http://example.com")
            request_count += 1
        throughput = request_count / 60
        return {"throughput": throughput}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/error-rate")
def measure_error_rate():
    try:
        log_file = "/var/log/myapp/error.log"
        if os.path.exists(log_file):
            with open(log_file, "r") as file:
                logs = file.readlines()
            error_count = len(logs)
            return {"error_count": error_count}
        else:
            raise HTTPException(status_code=500, detail=f"{log_file} file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/long-running-queries")
def get_long_running_queries():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=DictCursor)
        cursor.execute("SELECT pid, query, state, age(now(), query_start) AS runtime FROM pg_stat_activity WHERE state != 'idle' ORDER BY runtime DESC LIMIT 5;")
        long_running_queries = cursor.fetchall()
        conn.close()
        return {"long_running_queries": long_running_queries}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/query-execution-time")
def get_query_execution_time(query: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        start_time = time.time()
        cursor.execute(query)
        end_time = time.time()
        execution_time = end_time - start_time
        conn.close()
        return {"execution_time": execution_time}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/query-cache-hit-ratio")
def get_query_cache_hit_ratio():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=DictCursor)
        cursor.execute("SELECT sum(blks_hit) / (sum(blks_hit) + sum(blks_read)) AS cache_hit_ratio FROM pg_stat_database;")
        cache_hit_ratio = cursor.fetchone()
        conn.close()
        return {"cache_hit_ratio": cache_hit_ratio}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

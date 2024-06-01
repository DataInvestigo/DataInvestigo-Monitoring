from fastapi import APIRouter, HTTPException
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

@router.get("/database-version")
def get_database_version():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        conn.close()
        return {"database_version": db_version}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/patch-management")
def get_patch_management():
    try:
        # Assuming a table 'pg_patches' that keeps track of applied patches
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=DictCursor)
        cursor.execute("SELECT * FROM pg_patches;")
        applied_patches = cursor.fetchall()
        # Here we would compare with the known patches list
        # For demonstration, assume we have a known patches list
        known_patches = [
            {"patch_id": 1, "patch_name": "patch_1", "applied": False},
            {"patch_id": 2, "patch_name": "patch_2", "applied": False}
        ]
        for patch in known_patches:
            for applied_patch in applied_patches:
                if patch["patch_id"] == applied_patch["patch_id"]:
                    patch["applied"] = True
                    break
        conn.close()
        return {"patch_management": known_patches}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

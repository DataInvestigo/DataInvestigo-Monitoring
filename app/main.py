from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_router import api_router

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",  # Your React app's address
    "http://localhost:8000",  # If you are running React and FastAPI on the same local machine
    # Add more origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows these origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (POST, GET, PUT, DELETE, etc)
    allow_headers=["*"],  # Allows all headers
)

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# @app.get("/", response_class=HTMLResponse)
# def read_root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request, "title": "InfraMonitoring", "message": "Welcome to InfraMonitoring"})

# Include API routers
app.include_router(api_router)


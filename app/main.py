from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from .database import Base, engine
from .routes import student, auth
from . import models

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management System")

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (dev only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- ROUTES ----------------
app.include_router(auth.router)
app.include_router(student.router)

# ---------------- STATIC FILES ----------------
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# ---------------- API TEST ROUTE ----------------
@app.get("/api-test")
def api_test():
    return {"message": "Student Management API Running Successfully 🚀"}

# ---------------- PAGES ----------------
@app.get("/")
def serve_login():
    return FileResponse("frontend/index.html")

@app.get("/dashboard")
def serve_dashboard():
    return FileResponse("frontend/dashboard.html")

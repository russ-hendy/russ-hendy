from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Personal Website API")

# CORS Configuration
# Allow the frontend (Vite default port or deployed URL) to communicate with this backend.
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    # Add your production AWS Amplify URL here later
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """
    Simple root endpoint.
    """
    return {"message": "Hello! The backend is up and running."}

@app.get("/api/status")
def get_status():
    return {"status": "ok", "project": "Russ Hendy Personal Site"}

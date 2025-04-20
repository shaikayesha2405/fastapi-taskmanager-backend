from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import tasks  # Assuming your task routes are here
from app.database import engine
from app.models import Base

# Create FastAPI app instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Create DB tables (if they don't already exist)
Base.metadata.create_all(bind=engine)

# Include the task routes
app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Task Manager API is up!"}

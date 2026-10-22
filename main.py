# Main file for ageless-backend

# import functionalities from other files & act as FastAPI host file

from fastapi import FastAPI

from pydantic import BaseModel, Field

import uvicorn
from mic01 import record

app = FastAPI(
    title="Ageless-Companion Backend",
    description=(
        "Testing Dynamic Backend for Ageless-Companion"
    ),
    version="0.0.2",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Request Body validation? Why here?- Just for Demo
# later, Pydantic Schemata (Models) inside a separate models.py file

# Request Body validation
class RecordingRequest(BaseModel):
    duration_seconds: int = Field(ge=1, le=120, strict=True)


@app.get("/")
def root():
    """Backend usage Instructions"""
    return{
        "message": "Backend for Ageless-Companion running 🏃‍♂️",
        "Mic_endpoint": "Use POST /record",
        "duration_limits": {
            "max": 120,
            "min": 1,
        },
    }


# POST
@app.post("/record")
def mic(request: RecordingRequest):
    """Agless-Companion's Mic module endpoint, using Local machine's mic"""
    # Imported from ageless_audio package (recorder module)
    return record(request.duration_seconds)

if __name__== "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8090, reload=True)
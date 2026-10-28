# -----------------------------
# Main file for ageless-backend
# -----------------------------


# import functionalities from other files & act as FastAPI host file
# Importing Mic functionality
from mic01 import record
# Importing Playback functionality

# import play01
# Why from play01 import * fails?
# from play01 import *
from play01 import list_recordings, get_recording

# from play01 import list_recordings, get_recording
from fastapi import HTTPException
from fastapi.responses import FileResponse




# importing FastAPI and other dependencies
from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn

# FastAPI
app = FastAPI(
    title="Ageless-Companion Backend",
    description=(
        "Testing Dynamic Backend for Ageless-Companion"
    ),
    version="0.0.3",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)


# Request Body validation? Why here?- Just for Demo
# later, Pydantic Schemata (Models) inside a separate models.py file

# Request Body validation
class RecordingRequest(BaseModel):
    duration_seconds: int = Field(ge=1, le=60, strict=True)


# Visible at '/' route
@app.get("/")
def root():
    """Backend usage Instructions"""
    return {
        "message": "Backend for Ageless-Companion running 🏃‍♂️",
        "mic_endpoint": "Use POST /record",
        # duration_limits in seconds
        "duration_limits": {
            "max": 60,
            "min": 1,
        },
        "records_endpoints": "Use '/recordings' & /recordings/{file_name}'"
    }


# POST for audio recordingg
@app.post("/record")
def mic(request: RecordingRequest):
    """Agless-Companion's mic module endpoint, using local machine's mic"""
    # Imported from ageless_audio package (recorder module)
    return record(request.duration_seconds)




#⁉️ Standardise whether Path Parameters or Query Parameters are to be used!

# Serve recorded audio-files 🍽️

# ⚠️- Think!
# Playback of the recordings?
# Which method?- POST OR QUERY OR GET ?? I think QUERY
# ‼️ FastAPI does NOT have Native Support for QUERY
# using QUERY with FastAPI workaround? -> GET for now

# All records
# @app.get("/recordings")
# def access_audio():
#     """Endpoint for accessing all availabel recordings"""
#     return play01.voice_files

@app.get("/recordings")
def access_audio():
    """Return all available recording filenames."""
    return list_recordings()




@app.get("/recordings/{record_name}")
def access_record(record_name: str):
    """Serve a specific WAV recording."""
    file_path = get_recording(record_name)
    return FileResponse(
        path=file_path,
        media_type="audio/wav",
    )




# Specific records
# Path Param
# @app.get("/recordings/{record_name}")
# def access_record(record_name):
#     """Endpoint for accessing 'specific' recordings, as Path Param"""
#     return play01.voice_files[record_name]

# Query Param ?

# Exceptions will be delt with later, in future updates 🤗


if __name__== "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8090, reload=True)
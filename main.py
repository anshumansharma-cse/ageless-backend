# Main file for ageless-backend

# import functionalities from other files & act as FastAPI host file

from fastapi import FastAPI
import uvicorn
from mic01 import record

app = FastAPI(
    title="Ageless-Companion Backend",
    description=(
        "Testing Dynamic Backend for Ageless-Companion"
    ),
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def root():
    """Root"""
    return{
        "Use": "Root for ageless backend",
        "Mic": "Use /record path for accessing mic 🎙️"
    }

@app.get("/record")
def mic():
    """Agless-Companion's mic module """
    # Imported from ageless_audio package (recorder module)
    return record()

if __name__== "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8090, reload=True)
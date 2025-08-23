from fastapi import FastAPI
from .routers.tracking_router import tracking_router
app = FastAPI(title="My API", version="1.0.0")



app.include_router(tracking_router)  # Include the tracking router


# Endpoint gốc để kiểm tra
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Object Tracking API!"}
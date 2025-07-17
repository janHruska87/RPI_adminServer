from fastapi import FastAPI
from api.v1.api import router
from config.config import settings
from db import session
from db.models import Base
from models.device import Device
from models.log import DeviceStatusLog
import os

app = FastAPI(title="RPi Management Server")

os.makedirs(settings.IMAGE_UPLOAD_DIR, exist_ok=True)
os.makedirs(settings.CONFIG_UPLOAD_DIR, exist_ok=True)

@app.on_event("startup")
async def startup():
    async with session.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(router, prefix="/api/v1")


from app.db import models, session
from app.models.device import Device
from app.models.log import DeviceStatusLog

@app.on_event("startup")
async def startup():
    async with session.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

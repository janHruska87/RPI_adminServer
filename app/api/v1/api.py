from fastapi import APIRouter
from . import config, images, devices, status_logs
router = APIRouter()
router.include_router(config.router, prefix="/config", tags=["Config Files"])
router.include_router(images.router, prefix="/images", tags=["Images"])
router.include_router(devices.router, prefix="/devices", tags=["Devices"])
router.include_router(status_logs.router, prefix="/status-logs", tags=["Status Logs"])

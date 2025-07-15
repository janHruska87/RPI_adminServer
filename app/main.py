from fastapi import FastAPI
from app.api.v1 import routes_users, routes_devices, routes_uploads

app = FastAPI(title="RPI Management API")

app.include_router(routes_users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(routes_devices.router, prefix="/api/v1/devices", tags=["Devices"])
app.include_router(routes_uploads.router, prefix="/api/v1/uploads", tags=["Uploads"])

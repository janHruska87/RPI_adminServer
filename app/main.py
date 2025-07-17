from app.routers.v1 import rpi_units, upload
from fastapi import FastAPI

import app.routers.v1

app2 = FastAPI()

# Mountování statických souborů (např. CSS/JS) – OK
app2.mount("/", app=app2, name="test")

app2.include_router(rpi_units.router,prefix="/routers/v1")
app2.include_router(upload.router, prefix="/routers/v1")

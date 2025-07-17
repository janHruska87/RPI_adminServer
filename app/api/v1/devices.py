from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.device import DeviceCreate
from app.models.device import Device
from sqlalchemy import select, delete

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def list_devices(request: Request, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Device))
    devices = result.scalars().all()
    return templates.TemplateResponse("devices.html", {"request": request, "devices": devices})

@router.post("/add/")
async def add_device(name: str = Form(...), description: str = Form(""), db: AsyncSession = Depends(get_db)):
    new_device = Device(name=name, description=description)
    db.add(new_device)
    await db.commit()
    return RedirectResponse(url="/api/v1/devices/", status_code=303)

@router.post("/delete/{device_id}")
async def delete_device(device_id: int, db: AsyncSession = Depends(get_db)):
    await db.execute(delete(Device).where(Device.id == device_id))
    await db.commit()
    return RedirectResponse(url="/api/v1/devices/", status_code=303)

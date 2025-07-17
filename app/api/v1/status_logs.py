from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.log import StatusLogCreate, StatusLogOut
from models.log import DeviceStatusLog
from db.session import get_db
from sqlalchemy import select

router = APIRouter()

@router.post("/", response_model=StatusLogOut)
async def create_log(log: StatusLogCreate, db: AsyncSession = Depends(get_db)):
    new_log = DeviceStatusLog(**log.dict())
    db.add(new_log)
    await db.commit()
    await db.refresh(new_log)
    return new_log

@router.get("/", response_model=list[StatusLogOut])
async def get_logs(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(DeviceStatusLog))
    return result.scalars().all()

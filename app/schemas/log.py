from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from datetime import datetime
class StatusLogCreate(BaseModel):
    device_id: int
    status: str
    message: Optional[str] = None

class StatusLogOut(BaseModel):
    id: int
    device_id: int
    status: str
    message: Optional[str] = None
    timestamp: datetime

    class Config:
        orm_mode = True

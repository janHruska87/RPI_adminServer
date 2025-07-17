from pydantic import BaseModel

class DeviceCreate(BaseModel):
    name: str
    description: str

class DeviceOut(BaseModel):
    id: int
    name: str
    description: str

class Config:
        orm_mode = True

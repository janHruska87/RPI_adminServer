from pydantic import BaseModel

class RPIUnitCreate(BaseModel):
    name: str
    ip_address: str

class RPIUnitUpdate(BaseModel):
    name: str
    ip_address: str

class RPIUnitOut(RPIUnitCreate):
    id: int


class Config:
        orm_mode = True

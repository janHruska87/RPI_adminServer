from sqlalchemy import Column, Integer, String
from .db import Base

class RPIUnit(Base):
    __tablename__ = "rpi_units"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ip_address = Column(String, index=True)

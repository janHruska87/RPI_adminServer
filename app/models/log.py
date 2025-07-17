from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from app.db.models import Base
class DeviceStatusLog(Base):
    __tablename__ = "device_status_logs"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"))
    status = Column(String)
    message = Column(String, nullable=True)
    timestamp = Column(DateTime, default=func.now())

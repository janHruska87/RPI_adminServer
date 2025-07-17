from sqlalchemy.orm import Session
from app import models, schemas

def get_rpi_units(db: Session):
    return db.query(models.RPIUnit).all()

def get_rpi_unit(db: Session, unit_id: int):
    return db.query(models.RPIUnit).filter(models.RPIUnit.id == unit_id).first()

def create_rpi_unit(db: Session, unit: schemas.RPIUnitCreate):
    db_unit = models.RPIUnit(**unit.dict())
    db.add(db_unit)
    db.commit()
    db.refresh(db_unit)
    return db_unit

def update_rpi_unit(db: Session, unit_id: int, unit: schemas.RPIUnitUpdate):
    db_unit = get_rpi_unit(db, unit_id)
    if db_unit:
        for key, value in unit.dict().items():
            setattr(db_unit, key, value)
        db.commit()
        db.refresh(db_unit)
    return db_unit

def delete_rpi_unit(db: Session, unit_id: int):
    db_unit = get_rpi_unit(db, unit_id)
    if db_unit:
        db.delete(db_unit)
        db.commit()
    return db_unit

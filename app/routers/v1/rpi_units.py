from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import app.crud as crud
import app.schemas as schemas
from app.db import SessionLocal, Base, engine

Base.metadata.create_all(bind=engine)
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.RPIUnitOut])
def list_units(db: Session = Depends(get_db)):
    return crud.get_rpi_units(db)

@router.post("/", response_model=schemas.RPIUnitOut)
def create_unit(unit: schemas.RPIUnitCreate, db: Session = Depends(get_db)):
    return crud.create_rpi_unit(db, unit)

@router.put("/{unit_id}", response_model=schemas.RPIUnitOut)
def update_unit(unit_id: int, unit: schemas.RPIUnitUpdate, db: Session = Depends(get_db)):
    db_unit = crud.update_rpi_unit(db, unit_id, unit)
    if db_unit is None:
        raise HTTPException(status_code=404, detail="Unit not found")
    return db_unit

@router.delete("/{unit_id}")
def delete_unit(unit_id: int, db: Session = Depends(get_db)):
    db_unit = crud.delete_rpi_unit(db, unit_id)
    if db_unit is None:
        raise HTTPException(status_code=404, detail="Unit not found")
    return {"message":"Deleted"}

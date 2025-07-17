from fastapi import APIRouter, UploadFile, File
from app.services.upload_service import save_file
import os

router = APIRouter()

UPLOAD_DIR = "uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("\config")
async def upload_config(file: UploadFile = File(...)):
    dest = os.path.join(UPLOAD_DIR, file.filename)
    await save_file(file, dest)
    return {"filename": file.filename}

@router.post("\image")
async def upload_image(file: UploadFile = File(...)):
    dest = os.path.join(UPLOAD_DIR, file.filename)
    await save_file(file, dest)
    return {"filename": file.filename}

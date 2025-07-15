import os
from fastapi import APIRouter, UploadFile, File, Form

router = APIRouter()

PICTURES_DIR = "pictures"
MODELS_DIR = "MLL_models"

os.makedirs(PICTURES_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)

@router.post("/image")
async def upload_image(device_id: str = Form(...), file: UploadFile = File(...)):
    filename = f"{device_id}_{file.filename}"
    path = os.path.join(PICTURES_DIR, filename)
    with open(path, "wb") as f:
        f.write(await file.read())
    return {"filename": filename}

@router.post("/model")
async def upload_model(device_id: str = Form(...), file: UploadFile = File(...)):
    if not file.filename.endswith(".mkd"):
        return {"error": "Invalid file type"}
    filename = f"{device_id}.mkd"
    path = os.path.join(MODELS_DIR, filename)
    with open(path, "wb") as f:
        f.write(await file.read())
    return {"filename": filename}

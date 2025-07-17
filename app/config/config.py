import os
from dotenv import load_dotenv
load_dotenv()
class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    IMAGE_UPLOAD_DIR = os.getenv("IMAGE_UPLOAD_DIR", "./images")
    CONFIG_UPLOAD_DIR = os.getenv("CONFIG_UPLOAD_DIR", "./config_files")

settings = Settings()

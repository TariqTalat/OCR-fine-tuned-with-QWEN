import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-1.5B-Instruct")
    GPU_ENABLED = os.getenv("GPU_ENABLED", "true").lower() == "true"
    MAX_IMAGE_SIZE = int(os.getenv("MAX_IMAGE_SIZE", "1600"))
    MAX_NEW_TOKENS = int(os.getenv("MAX_NEW_TOKENS", "1200"))
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.0"))</content>
<parameter name="filePath">d:\Projects\OCR + QWEN\app\config.py
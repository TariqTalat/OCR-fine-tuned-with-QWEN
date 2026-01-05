from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import tempfile
import os
from app.helpers.image_processing import preprocess_image
from app.helpers.ocr import perform_ocr
from app.helpers.text_normalization import normalize_text
from app.helpers.llm import LLMProcessor
from app.config import Config

router = APIRouter()

llm_processor = LLMProcessor()

@router.post("/process_invoice")
async def process_invoice(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        raise HTTPException(status_code=400, detail="Invalid file type. Only image files are allowed.")

    try:
        # Save uploaded file to temp
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
            temp_file.write(await file.read())
            temp_path = temp_file.name

        # Preprocess image
        original_img, preprocessed_img = preprocess_image(temp_path, Config.MAX_IMAGE_SIZE)

        # Perform OCR
        raw_lines, ocr_results = perform_ocr(preprocessed_img, Config.GPU_ENABLED)

        # Normalize text
        normalized_text = normalize_text(raw_lines)

        # Extract data with LLM
        invoice_data = llm_processor.extract_invoice_data(normalized_text)

        # Clean up temp file
        os.unlink(temp_path)

        return JSONResponse(content=invoice_data.dict())

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))</content>
<parameter name="filePath">d:\Projects\OCR + QWEN\app\controllers.py
# Invoice OCR API

A FastAPI-based service for extracting structured data from invoice images using OCR and LLM.

## Features

- Image preprocessing with OpenCV
- OCR using EasyOCR (Arabic and English support)
- Text normalization
- Structured data extraction with Qwen LLM
- RESTful API with FastAPI

## Setup

1. Install Python 3.11+
2. Create virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables in `.env` file
5. Run the application:
   ```bash
   python main.py
   ```

## API Usage

### Process Invoice

POST `/process_invoice`

Upload an image file (PNG, JPG, JPEG, BMP, TIFF) to extract invoice data.

Example using curl:
```bash
curl -X POST "http://localhost:8000/process_invoice" -F "file=@invoice.png"
```

Response:
```json
{
  "invoice_metadata": {
    "invoice_number": "...",
    "invoice_date": "...",
    ...
  },
  "line_items": [...],
  "financial_summary": {...}
}
```

## Configuration

Edit `.env` file to configure:
- MODEL_NAME: LLM model to use
- GPU_ENABLED: Enable GPU for inference
- MAX_IMAGE_SIZE: Maximum image dimension for resizing
- MAX_NEW_TOKENS: Maximum tokens for LLM generation
- TEMPERATURE: Sampling temperature</content>
<parameter name="filePath">d:\Projects\OCR + QWEN\README.md
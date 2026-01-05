from fastapi import FastAPI
from app.controllers import router

app = FastAPI(title="Invoice OCR API", version="1.0.0")

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Invoice OCR API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)</content>
<parameter name="filePath">d:\Projects\OCR + QWEN\app\main.py
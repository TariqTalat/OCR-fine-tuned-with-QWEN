import easyocr
import numpy as np
from typing import List, Tuple

def perform_ocr(image: np.ndarray, gpu: bool = True) -> Tuple[List[str], List[Tuple]]:
    reader = easyocr.Reader(['ar', 'en'], gpu=gpu)
    ocr_results = reader.readtext(image, detail=1, paragraph=False)
    # ocr_results is list of tuples: (bbox, text, confidence)
    raw_lines = [t[1].strip() for t in ocr_results if t[1].strip()]
    return raw_lines, ocr_results</content>
<parameter name="filePath">d:\Projects\OCR + QWEN\app\helpers\ocr.py
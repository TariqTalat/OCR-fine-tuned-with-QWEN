import cv2
import numpy as np
import os
from typing import Tuple

def preprocess_image(path: str, resize_max: int = 1600) -> Tuple[np.ndarray, np.ndarray]:
    img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR) \
          if os.name == 'nt' else cv2.imread(path)
    if img is None:
        with open(path, "rb") as f:
            arr = np.frombuffer(f.read(), np.uint8)
            img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    h, w = img.shape[:2]
    if max(h, w) > resize_max:
        scale = resize_max / max(h, w)
        img = cv2.resize(img, (int(w*scale), int(h*scale)), interpolation=cv2.INTER_AREA)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.fastNlMeansDenoising(gray, None, 30, 7, 21)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 31, 2)
    return img, thresh</content>
<parameter name="filePath">d:\Projects\OCR + QWEN\app\helpers\image_processing.py
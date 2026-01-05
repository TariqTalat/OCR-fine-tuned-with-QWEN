import re
from typing import List

ARABIC_DIGITS = {'٠': '0', '١': '1', '٢': '2', '٣': '3', '٤': '4', '٥': '5', '٦': '6', '٧': '7', '٨': '8', '٩': '9'}

def normalize_digits(s: str) -> str:
    for ar, en in ARABIC_DIGITS.items():
        s = s.replace(ar, en)
    return s

def normalize_punctuation(s: str) -> str:
    s = s.replace('،', ',').replace('٫', '.').replace('٬', ',')
    return s

def clean_whitespace(s: str) -> str:
    s = re.sub(r'\u200f', '', s)
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n{2,}', '\n', s)
    return s.strip()

def normalize_numbers(s: str) -> str:
    # Convert arabic digits, normalize commas/dots to unified decimal separator,
    s = normalize_digits(s)
    s = normalize_punctuation(s)
    s = re.sub(r'(?<=\d)[,](?=\d{3}\b)', '', s)
    s = re.sub(r'(?<=\d)[.](?=\d{3}\b)', '', s)
    return s

def normalize_line(s: str) -> str:
    s = s.strip()
    s = normalize_digits(s)
    s = normalize_punctuation(s)
    s = normalize_numbers(s)
    s = clean_whitespace(s)
    return s

def normalize_text(raw_lines: List[str]) -> str:
    normalized_lines = [normalize_line(l) for l in raw_lines if l.strip()]
    return "\n".join(normalized_lines)</content>
<parameter name="filePath">d:\Projects\OCR + QWEN\app\helpers\text_normalization.py
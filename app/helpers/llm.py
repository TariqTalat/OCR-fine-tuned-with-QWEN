import json
import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from app.config import Config
from app.models import InvoiceData

INVOICE_SCHEMA = {
    "invoice_metadata": {
        "invoice_number": "",
        "invoice_date": "",
        "seller_name": "",
        "buyer_name": "",
        "commercial_registration_number": "",
        "address": ""
    },
    "line_items": [
        {
            "description": "",
            "quantity": "",
            "unit_price": "",
            "total_price": ""
        }
    ],
    "financial_summary": {
        "subtotal": "",
        "vat_percentage": "",
        "vat_amount": "",
        "final_total": ""
    }
}

SYSTEM_PROMPT = """
You are a strict information extraction engine.
You extract structured data from OCR text.

Rules:
- Use ONLY the provided OCR text
- Fill values ONLY if explicitly present
- Do NOT guess
- Do NOT change schema keys
- Return VALID JSON ONLY
- Empty string "" if value not found
"""

class LLMProcessor:
    def __init__(self):
        self.model_name = Config.MODEL_NAME
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float16,
        )
        if Config.GPU_ENABLED and torch.cuda.is_available():
            self.model = self.model.to("cuda")
        self.model.eval()

    def extract_invoice_data(self, normalized_text: str) -> InvoiceData:
        user_prompt = f"""
Extract invoice information and fill the schema below.

SCHEMA:
{json.dumps(INVOICE_SCHEMA, ensure_ascii=False, indent=2)}

OCR TEXT:
{normalized_text}

Return ONLY JSON.
"""

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ]

        prompt = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=Config.MAX_NEW_TOKENS,
                temperature=Config.TEMPERATURE,
                do_sample=False,
            )

        llm_output = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        extracted = self.extract_json_from_fenced_block(llm_output)

        return InvoiceData(**extracted)

    def extract_json_from_fenced_block(self, text: str) -> dict:
        """
        Extract JSON from a ```json ... ``` fenced block.
        This is the safest method for LLM outputs.
        """
        pattern = r"```json\s*(\{.*?\})\s*```"
        matches = re.findall(pattern, text, re.DOTALL)

        if not matches:
            raise ValueError(" No fenced JSON block found")

        json_str = matches[-1]
        return json.loads(json_str)</content>
<parameter name="filePath">d:\Projects\OCR + QWEN\app\helpers\llm.py
from pydantic import BaseModel
from typing import List

class LineItem(BaseModel):
    description: str = ""
    quantity: str = ""
    unit_price: str = ""
    total_price: str = ""

class InvoiceMetadata(BaseModel):
    invoice_number: str = ""
    invoice_date: str = ""
    seller_name: str = ""
    buyer_name: str = ""
    commercial_registration_number: str = ""
    address: str = ""

class FinancialSummary(BaseModel):
    subtotal: str = ""
    vat_percentage: str = ""
    vat_amount: str = ""
    final_total: str = ""

class InvoiceData(BaseModel):
    invoice_metadata: InvoiceMetadata
    line_items: List[LineItem]
    financial_summary: FinancialSummary</content>
<parameter name="filePath">d:\Projects\OCR + QWEN\app\models.py
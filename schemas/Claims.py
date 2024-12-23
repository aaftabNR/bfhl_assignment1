from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class Claim(BaseModel):
    Id: str
    CreatedDate: date
    CaseNumber: str
    HAN: str
    BillAmount: Decimal
    Status: str
    AccountId: str

from pydantic import BaseModel

class Account(BaseModel):
    AccountId: str
    Name: str
    Age: int
    City: str
    State: str
    Pincode: str
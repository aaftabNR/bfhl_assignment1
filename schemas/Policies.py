from pydantic import BaseModel

class Policy(BaseModel):
    HAN: str
    PolicyName: str
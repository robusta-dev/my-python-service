from pydantic import BaseModel

def Service(BaseModel):
    name: str
    role: str
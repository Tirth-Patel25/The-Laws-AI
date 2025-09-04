from pydantic import BaseModel

class metadata(BaseModel):
    category: str
    id: str
    country: str
    state: str
    court: str
    year: str

class UserRequest(BaseModel):
    query: str
    metadata: metadata

from pydantic import BaseModel

class Parameter(BaseModel):
    id: int = None
    reference: str
    name: str
    description: str

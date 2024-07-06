from pydantic import BaseModel

class roles(BaseModel):
    id: int=None
    name: str
    state: int
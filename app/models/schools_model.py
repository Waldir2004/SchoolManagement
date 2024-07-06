from pydantic import BaseModel

class schools(BaseModel):
    id: int=None
    name: str
    state: int
    created_at: str=None
    
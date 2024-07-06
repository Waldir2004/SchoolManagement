from pydantic import BaseModel
from datetime import datetime
class activities(BaseModel):
    id: int=None
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    school_id:int
    state_id:int

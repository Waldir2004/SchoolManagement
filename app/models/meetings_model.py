from pydantic import BaseModel
from datetime import datetime, time
class meetings(BaseModel):
    id: int=None
    title:str
    description:str
    date:datetime
    time:time
    school_id:int
    state:int

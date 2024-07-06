from pydantic import BaseModel
class comments_activities(BaseModel):
    id: int=None
    activity_id:int
    user_id:int
    comment:str
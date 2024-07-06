from pydantic import BaseModel

class ParticipantActivity(BaseModel):
    id: int=None
    activity_id: int
    type_id: int
    user_id: int
    state: int
from pydantic import BaseModel

class ParticipantMeeting(BaseModel):
    id: int=None
    meeting_id: int
    type_id: int
    user_id: int
    state: int
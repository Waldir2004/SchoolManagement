from pydantic import BaseModel
class evidence_activities(BaseModel):
    id: int=None
    activity_id:int
    type_id:int
    uploaded_by:int
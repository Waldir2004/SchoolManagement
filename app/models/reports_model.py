from pydantic import BaseModel
class reports(BaseModel):
    id: int=None
    type_report_id:int
    reporter_id:int
    reported_user_id:int
    description:str
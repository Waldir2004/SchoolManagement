from pydantic import BaseModel
class reports_evidencies(BaseModel):
    id: int=None
    type_file_id:int
    uploaded_by:int
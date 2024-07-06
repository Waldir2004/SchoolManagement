from pydantic import BaseModel

class SchoolUser(BaseModel):
    id: int = None
    user_id: int
    school_id: int


from pydantic import BaseModel

class User(BaseModel):
    id: int = None
    role_id: int
    name: str
    last_name: str
    email: str
    phone: str
    document_type_id: int
    document_number: str
    password: str
    state: int

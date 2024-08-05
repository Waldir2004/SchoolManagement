from pydantic import BaseModel

class Auth(BaseModel):
    id: int=None
    email: str
    password: str
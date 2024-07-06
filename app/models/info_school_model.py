from pydantic import BaseModel

class SchoolInfo(BaseModel):
    id: int = None
    school_id: int
    name: str
    address: str
    phone: str
    email: str
    city_or_municipality_id: int
    director_id: int
    type_id: int
    website: str


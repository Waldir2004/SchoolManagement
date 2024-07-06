from pydantic import BaseModel

class ParameterValue(BaseModel):
    id: int = None
    parameter_id: int
    name: str
    description: str

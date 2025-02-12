from pydantic import BaseModel
from typing import Optional

class Program(BaseModel):
    name: str
    description: Optional[str]

class RegisterProgram(Program):
    pass
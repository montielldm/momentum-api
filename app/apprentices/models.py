from pydantic import BaseModel

class Apprentice(BaseModel):
    name: str
    lastname: str
    document_type: str
    document: str
    avatar: str
    email: str
    program: str

class RegisterApprentice(Apprentice):
    pass
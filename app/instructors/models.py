from pydantic import BaseModel

class Instructor(BaseModel):
    name: str
    lastname: str
    document_type: str
    document: str
    avatar: str
    email: str
    specialization: str
    resume: str
    experience: str

class RegisterInstructor(Instructor):
    pass
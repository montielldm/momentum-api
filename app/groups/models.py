from pydantic import BaseModel

class Group(BaseModel):
    name: str
    program: str

class RegisterGroup(Group):
    pass

class AddInstructorToGroup(BaseModel):
    instructor: str
    group: str

class AddApprenticeToGroup(BaseModel):
    apprentice: str
    group: str
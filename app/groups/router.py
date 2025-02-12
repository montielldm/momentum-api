from fastapi import APIRouter, Depends
from app.groups.services import (
    get_all_groups_service,
    get_groups_by_id_service,
    register_group_service,
    add_apprentice_to_group_service,
    add_instructor_to_group_service
)
from app.groups.models import (
    RegisterGroup,
    AddApprenticeToGroup,
    AddInstructorToGroup
)
from app.auth.utils import get_current_user

groups = APIRouter(
    prefix="/groups",
    tags=["Groups"]
)

@groups.get("")
def get_all_groups(user_id: str = Depends(get_current_user)):
    result = get_all_groups_service(user_id)
    return result

@groups.get("/{id}")
def get_group_by_id(id: str):
    result = get_groups_by_id_service(id)
    return result

@groups.post("")
def register_group(group: RegisterGroup):
    result = register_group_service(group)
    return result

@groups.post("/add-apprentice-to-group")
def add_apprentice_to_group(association: AddApprenticeToGroup):
    result = add_apprentice_to_group_service(association)
    return result

@groups.post("/add-instructor-to-group")
def add_instrutor_to_group(association: AddInstructorToGroup):
    result = add_instructor_to_group_service(association)
    return result
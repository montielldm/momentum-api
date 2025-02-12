from fastapi import APIRouter
from app.instructors.services import (
    get_all_instructors_service,
    get_instructor_by_id_service,
    register_instructor_service
)
from app.instructors.models import RegisterInstructor

instructors = APIRouter(
    prefix="/instructors",
    tags=["Instructors"]
)

@instructors.get("")
def get_all_instructors():
    result = get_all_instructors_service()
    return result

@instructors.get("/{id}")
def get_instructor_by_id(id: str):
    result = get_instructor_by_id_service(id)
    return result

@instructors.post("")
def register_instructor(instructor: RegisterInstructor):
    result = register_instructor_service(instructor)
    return result
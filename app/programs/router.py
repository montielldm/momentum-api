from fastapi import APIRouter
from app.programs.services import (
    get_all_programs_service,
    register_program_service,
    disable_program_service,
    get_program_by_id_service
)
from app.programs.models import RegisterProgram

programs = APIRouter(
    prefix="/programs",
    tags=["Programs"]
)

@programs.get("")
def get_all_subjects():
    result = get_all_programs_service()
    return result

@programs.get("/{id}")
def get_program_by_id(id: str):
    result = get_program_by_id_service(id)
    return result

@programs.post("")
def register_program(program: RegisterProgram):
    result = register_program_service(program)
    return result

@programs.put("/{id}")
def disable_program(id: str):
    result = disable_program_service(id)
    return result
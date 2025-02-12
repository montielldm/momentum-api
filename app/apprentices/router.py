from fastapi import APIRouter
from app.apprentices.services import (
    get_all_apprentices_service,
    get_apprentice_by_id_service,
    register_apprentice_service
)
from app.apprentices.models import RegisterApprentice

apprentices = APIRouter(
    prefix="/apprentices",
    tags=["Apprentices"]
)

@apprentices.get("")
def get_all_apprentices():
    result = get_all_apprentices_service()
    return result

@apprentices.get("/{id}")
def get_apprentice_by_id(id: str):
    result = get_apprentice_by_id_service(id)
    return result

@apprentices.post("")
def register_apprentice(apprentice: RegisterApprentice):
    result = register_apprentice_service(apprentice)
    return result
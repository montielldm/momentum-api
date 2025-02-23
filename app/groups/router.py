from fastapi import APIRouter, Depends
from app.auth.utils import get_current_user

groups = APIRouter(
    prefix="/groups",
    tags=["Groups"]
)

@groups.get("")
def get_all_groups(id: str = Depends(get_current_user)):
    return id
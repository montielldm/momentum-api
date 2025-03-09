from fastapi import APIRouter, Depends
from app.auth.utils import get_current_user
from app.groups.services import (
    get_all_groups_by_user_service,
    get_all_apprentices_by_group_service
)
from app.groups.serializers import (
    groups_by_user_serializer,
    users_by_group_serializer
)

groups = APIRouter(
    prefix="/groups",
    tags=["Groups"]
)

@groups.get("")
def get_all_groups(id: str = Depends(get_current_user)):
    groups = get_all_groups_by_user_service(id)
    return groups_by_user_serializer(groups)

@groups.get("/{group_id}/apprentices")
def get_all_apprentices_by_group(group_id: str, id: str = Depends(get_current_user)):
    apprentices = get_all_apprentices_by_group_service(group_id)
    return users_by_group_serializer(apprentices)
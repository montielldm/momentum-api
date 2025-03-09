from providers.database import ConnectDatabase
from sqlalchemy import select
from app.groups.models import Group
from app.users.services import (
    get_user_by_id_service
)
from app.groups.exceptions import (
    GroupNotFound
)

session = ConnectDatabase.getInstance()

def get_all_groups_by_user_service(user_id: str):
    user = get_user_by_id_service(user_id)
    groups = user.groups
    return groups

def get_all_apprentices_by_group_service(group_id: str):
    group = session.get(Group, group_id)
    if not group:
        GroupNotFound()
    
    apprentices = group.apprentices
    return apprentices
    
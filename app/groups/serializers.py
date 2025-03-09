from app.groups.models import Group
from typing import List
from app.users.models import User

def group_by_user_serializer(group: Group) -> dict:
    return {
        "id": group.id,
        "name": group.name,
        "modality": group.modality,
        "description": group.description,
        "program": {
            "id": group.program.id,
            "code": group.program.code,
            "type":group.program.type,
            "duration": group.program.duration,
            "timing_system": group.program.timing_system,
            "name": group.program.name
        },
        "amount_apprentinces": len(group.apprentices),
        "amount_instructors": len(group.instructors)
    }

def groups_by_user_serializer(groups: List[Group]) -> List:
    return [group_by_user_serializer(group) for group in groups]

def user_by_group_serializer(user: User) -> dict:
    return {
        "id": user.id,
        "name": user.name,
        "lastname": user.lastname,
        "avatar": user.avatar,
        "email": user.email,
        "document_type": user.document_type,
        "document": user.document
    }

def users_by_group_serializer(users: List[User]) -> list:
    return [user_by_group_serializer(user) for user in users]
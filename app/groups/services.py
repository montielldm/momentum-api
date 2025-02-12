from providers.supabase import client
from app.groups.models import RegisterGroup, AddInstructorToGroup, AddApprenticeToGroup
from nanoid import generate

def get_all_groups_service(user_id: str):
    user = client.table("users").select("*").eq("auth", user_id).single().execute()
    groups_users = client.table("groups_users").select("group(*, user(id, name, lastname, email, avatar), program(id, name))").eq("user", user.data["id"]).execute()
    
    groups = [group["group"] for group in groups_users.data]

    return groups

    

def get_groups_by_id_service(id: str):
    result = client.table("groups").select("*").eq("id", id).execute()
    return result.data

def register_group_service(group: RegisterGroup):
    result = client.table("groups").insert({
        "name": group.name,
        "program": group.program,
        "code": generate(size=12)
    }).execute()

    return result.data

def add_instructor_to_group_service(association: AddInstructorToGroup):
    result = client.table("instructors_groups").insert({
        "instructor": association.instructor,
        "group": association.group
    }).execute()

    return result.data

def add_apprentice_to_group_service(association: AddApprenticeToGroup):
    result = client.table("apprentices_groups").insert({
        "apprentice": association.apprentice,
        "group": association.group
    }).execute()

    return result.data
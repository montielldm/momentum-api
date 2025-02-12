from providers.supabase import client
from app.instructors.models import RegisterInstructor

def get_all_instructors_service():
    results = client.table("instructors").select("*").execute()
    return results.data

def get_instructor_by_id_service(id: str):
    result = client.table("instructors").select("*").eq("id", id).execute()
    return result.data

def register_instructor_service(instructor: RegisterInstructor):
    result = client.table("instructors").insert({
        "name": instructor.name,
        "lastname": instructor.lastname,
        "document_type": instructor.document_type,
        "document": instructor.document,
        "avatar": instructor.avatar,
        "email": instructor.email,
        "specialization": instructor.specialization,
        "resume": instructor.resume,
        "experience": instructor.experience,
    }).execute()

    return result.data
from providers.supabase import client
from app.programs.models import RegisterProgram

def get_all_programs_service():
    result = client.table("programs").select("*").execute()
    return result.data

def get_program_by_id_service(id: str):
    result = client.table("programs").select("*").eq("id", id).execute()
    return result.data

def register_program_service(program: RegisterProgram):
    result = client.table("programs").insert({
        "name": program.name,
        "description": program.description
    }).execute()
    
    return result.data

def disable_program_service(id: str):
    result = client.table("programs").update({
        "status": "inactive"
    }).eq("id", id).execute()

    return result.data
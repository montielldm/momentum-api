from providers.supabase import client
from app.apprentices.models import RegisterApprentice

def get_all_apprentices_service():
    results = client.table("apprentices").select("*").execute()
    return results.data

def get_apprentice_by_id_service(id: str):
    result = client.table("apprentices").select("*").eq("id", id).execute()
    return result.data

def register_apprentice_service(apprentice: RegisterApprentice):
    result = client.table("apprentices").insert({
        "name": apprentice.name,
        "lastname": apprentice.lastname,
        "document_type": apprentice.document_type,
        "document": apprentice.document,
        "avatar": apprentice.avatar,
        "email": apprentice.email,
        "program": apprentice.program
    }).execute()

    return result.data
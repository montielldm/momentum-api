from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from providers.supabase import client
from app.auth.utils import get_current_user

auth = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@auth.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    response = client.auth.sign_in_with_password({
        "email": form_data.username,
        "password": form_data.password
    })

    if not response:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas")
    
    return response.session

@auth.get("/user")
def user(user_id: str = Depends(get_current_user)):
    user = client.table("users").select("*, roles(name, created_at, id)").eq("auth", user_id).single().execute() 
    return user
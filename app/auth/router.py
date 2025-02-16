from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.services import (
    authenticate_user_service
)
from app.auth.exceptions import (
    UnauthorizedUser
)
from app.auth.utils import (
    create_access_token,
    create_refresh_token,
    verify_refresh_token_service
)
from app.users.services import (
    get_user_by_id
)


auth = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@auth.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_id = authenticate_user_service(form_data.username, form_data.password)

    if user_id is None:
        UnauthorizedUser()
    
    access_token = create_access_token({"sub": str(user_id)})
    refresh_token = create_refresh_token({"sub": str(user_id)})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@auth.post("/refresh-token")
def refresh(refresh_token: str):
    user_id = verify_refresh_token_service(refresh_token)
    user = get_user_by_id(user_id)

    access_token = create_access_token({"sub": str(user.id)})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

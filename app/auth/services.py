from providers.database import ConnectDatabase
from sqlalchemy.exc import PendingRollbackError
from sqlalchemy import select
from app.users.services import (
    get_user_by_document_service,
    get_user_by_id_service
)
from app.auth.utils import (
    verify_password,
    hash_password
)

session = ConnectDatabase.getInstance()

def authenticate_user_service(document: str, password: str):
    user = get_user_by_document_service(document)
    
    if not verify_password(password, user.password):
        return None
    
    return user.id

def reset_password_service(user_id: str, new_password: str):
    user = get_user_by_id_service(user_id)
    hashed_password = hash_password(new_password)

    user.password = hashed_password
    session.commit()
    session.refresh(user)
    return user
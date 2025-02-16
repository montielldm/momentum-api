from providers.database import ConnectDatabase
from sqlalchemy.exc import PendingRollbackError
from sqlalchemy import select
from app.users.services import (
    get_user_by_document_service
)
from app.auth.utils import (
    verify_password
)

session = ConnectDatabase.getInstance()

def authenticate_user_service(document: str, password: str):
    user = get_user_by_document_service(document)
    
    if not verify_password(password, user.password):
        return None
    
    return user.id
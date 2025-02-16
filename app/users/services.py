import uuid
from sqlalchemy import select
from app.users.models import User
from app.users.exceptions import (
    UserNotFound
)
from providers.database import ConnectDatabase
from sqlalchemy.exc import PendingRollbackError


session = ConnectDatabase.getInstance()

def get_user_by_id(id: str):
    try:
        result = session.get(User, id)
        if result is None:
            UserNotFound()

        return result
    except PendingRollbackError as e:
        session.rollback()

def get_user_by_email_service(email: str):
    try:
        stmt = select(User).where(User.email == email)
        result = session.scalars(stmt).first()
        if result is None:
            UserNotFound()

        return result
    except PendingRollbackError as e:
        session.rollback()

def get_user_by_document_service(document: str):
    try:
        stmt = select(User).where(User.document == document)
        result = session.scalars(stmt).first()
        if result is None:
            UserNotFound()

        return result
    except PendingRollbackError as e:
        session.rollback()

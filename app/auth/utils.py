import os
from jose import jwt, JWTError
from dotenv import load_dotenv
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta, timezone
from app.auth.exceptions import CouldNotValidateCredentials

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
SECRET_KEY_REFRESH = os.getenv('SECRET_KEY_REFRESH')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
REFRESH_TOKEN_EXPIRE_DAYS = 7

oauth2scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # Changed days to minutes
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY_REFRESH, algorithm=ALGORITHM)
    return encode_jwt

def get_current_user(token: str = Depends(oauth2scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Token inválido"
            )
        
        return user_id
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail=str(e)
        )

def verify_refresh_token_service(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY_REFRESH, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            CouldNotValidateCredentials()
    
        return user_id
    except JWTError:
        CouldNotValidateCredentials()
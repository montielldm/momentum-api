import os
from jose import jwt
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

load_dotenv()

SUPABASE_SECRET = os.getenv('SUPABASE_SECRET')
ALGORITHM = "HS256"
oauth2scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token = Depends(oauth2scheme)):
    try:
        payload = jwt.decode(token, SUPABASE_SECRET, algorithms=["HS256"], options={"verify_aud": False})
        user_id = payload.get('sub')

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Token inválido d"
            )
        
        return user_id

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail=str(e)
        )
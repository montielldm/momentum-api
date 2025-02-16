from fastapi import HTTPException, status

def UserNotFound():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="USER_NOT_FOUND"
    )
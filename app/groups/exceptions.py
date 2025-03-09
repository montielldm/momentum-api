from fastapi import status, HTTPException

def GroupNotFound():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="GROUP_NOT_FOUND"
    )
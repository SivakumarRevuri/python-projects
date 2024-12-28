from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.connections.database import get_db
from passlib.context import CryptContext
from src.models.users import User

bcrypt_context = CryptContext(schemes=["bcrypt"])

router = APIRouter(prefix="/auth", tags=["auth"])

SECURITY_KEY = "3add07950130eee62cb0f20a472b6491"
ALGORITHM = "HS256"


@router.post("/")
async def get_token(
    request: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
):
    return request.username


async def get_encrypted_password(password: str):
    return bcrypt_context.hash(password)


async def authenticate_user(
    username: str, password: str, db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()

    if user is None or not bcrypt_context.verify(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )

    return user

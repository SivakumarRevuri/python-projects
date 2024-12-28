from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.schemas.request.user import CreateUser
from src.connections.database import get_db
from src.models.users import User
from src.routers.auth import authenticate_user, get_encrypted_password

router = APIRouter(prefix="/user", tags=["user"], dependencies=[Depends(authenticate_user)])

from typing import Annotated
db_connection = Annotated[Session, Depends(get_db)]

@router.post("/")
async def create_user(data: CreateUser, db: db_connection):
    try:
        user = User(
            username=data.username,
            password= await get_encrypted_password(data.password),
            email=data.email,
            is_activate=True,
            role=data.role,
        )
        db.add(user)
        db.commit()

        return JSONResponse(
            content="User created successfully!", status_code=status.HTTP_201_CREATED
        )
    except IntegrityError as ie:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ie))
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error occured while creating the user. \n {ex}",
        )

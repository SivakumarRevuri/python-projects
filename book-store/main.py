from fastapi import FastAPI
from src.connections.database import Base, engine
from src.routers.auth import router as auth_router
from src.routers.user_router import router as user_router
from src.routers.todos_router import router as todos_router

app = FastAPI(title="BookStore")

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(todos_router, prefix="/todos", tags=["todos"])


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import FRONTEND_URL
from routers import items

app = FastAPI(
    title="Менеджер задач",
    description="Етот API может отдавать список задач, создавать задачи и искать задачу по id"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI application"}
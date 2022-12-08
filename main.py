# Python
from enum import Enum
from typing import Optional

# Pydantic
from pydantic import BaseModel, Field, EmailStr

# Fastapi
from fastapi import FastAPI, Body

app = FastAPI()


class Careers(Enum):
    sys = "sys"
    abo = "abo"


class Student(BaseModel):
    university: str = Field(default=..., example="unisinu")
    career: Careers = Field(default=..., example="sys")


class User(BaseModel):
    name: str = Field(default=None, example="victor")
    email: EmailStr = Field(default=..., example="me@local.co")
    ega: int = Field(default=None, example=20)
    students: Optional[list[Student]]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/hello", response_model=User)
async def say_hello(user: User = Body(default=...)) -> User:
    return user

# raise HTTPException(status_code=404, detail=f"Student {id} not found")

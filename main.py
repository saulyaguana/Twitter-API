# Python
from uuid import UUID
from datetime import date
from typing import Optional
# Pydantic
from pydantic import BaseModel
from pydantic import Field, EmailStr

# FastAPI
from fastapi import FastAPI

app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Filed(
        ...,
        min_length=9,
    )

class User(UserBase):
    
    
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optinal[date] = Field(default=None)

class Twitt():
    pass


@app.get(path="/")
def home():
    return {"Twitter API": "Working"}
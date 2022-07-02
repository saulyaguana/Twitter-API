# Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List
# Pydantic
from pydantic import BaseModel
from pydantic import Field, EmailStr

# FastAPI
from fastapi import FastAPI, status

app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=9,
        max_length=64
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
    birth_date: Optional[date] = Field(default=None)

class Twitt():
    tweet_id: UUID = Field(...) #Estos son atributos
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

#Path Operations

@app.get(path="/")
def home():
    return {"Twitter API": "Working"}

## Users
@app.post(
    path="/signup",
    responsive_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register an User",
    tags=["Users"]
)
def signup():
    pass

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_0K,
    summary="Login an user",
    tags=["Users"]
)
def login():
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_0K,
    summary="Show user",
    tags=["Users"]
)
def show_all_users():
    pass

@app.get(
    path="/users/{user_id}",
    response_model= User,
    status_code=status.HTTP_200_0K,
    summary="Show a user",
    tags=["Users"]
)
def show_a_user():
    pass


@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_0K,
    summary="Delete User",
    tags=["Users"]
)
def delete_a_user():
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_0K,
    summary="Update an user",
    tags=["Users"]
)
def update_a_user():
    pass


## Tweets

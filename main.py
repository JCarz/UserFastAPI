from http.client import UNPROCESSABLE_ENTITY
from os import stat
from uuid import UUID, uuid4
from fastapi import FastAPI,HTTPException
from typing import List, Union
from models import Gender, Roles, User

app = FastAPI()

db: List[User] = [
    User(
        id = UUID("fe60935b-8b2c-4277-a37b-eba8f055073f"),
        f_name = "John",
        l_name = "Doe",
        gender = Gender.male,
        roles = [Roles.admin]
    )
    ,
    User(
        id = UUID("860a49d0-11d9-4cae-95f5-a0e2b83df0b5"),
        f_name = "Jaylen",
        l_name = "Carroll",
        m_name = "I",
        gender = Gender.male,
        roles = [Roles.student,Roles.admin]
    )
] # This will act as our database which is a list containing User with a base modle of each variable type and a list of roles for each user in the list. This is also the blueprint of the user model.



@app.get("/")
async def head_root():
    return {"Hello": "Jay"} #JSON Object

@app.get("/api/v1/users")
async def fetch_users(): # Gets all users from the database list
    return db

@app.post("/api/v1/users")
async def create_user(user: User): # This is the body of the request
    db.append(user)
    return {"id" : user.id} # No need to have id in the body of the request.

@app.delete("/api/v1/users/{user_id}")# Path variable
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException( # This is the error message if the user is not found
        status_code=404, 
        detail=f"user with id {user_id} not found"
        )
        
from uuid import UUID, uuid4
from fastapi import FastAPI,HTTPException
from typing import List
from models import Gender, Role, User, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(
        id = UUID("fe60935b-8b2c-4277-a37b-eba8f055073f"),
        f_name = "John",
        l_name = "Doe",
        gender = Gender.male,
        roles = [Role.admin]
    ),
    User(
        id = UUID("860a49d0-11d9-4cae-95f5-a0e2b83df0b5"),
        f_name = "Jaylen",
        l_name = "Carroll",
        m_name = "I",
        gender = Gender.male,
        roles = [Role.student,Role.admin]
    )
]
# This will act as our database which is a list containing User with a base modle of each variable type and a list of roles for each user in the list. This is also the blueprint of the user model.

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

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id:UUID):
    for user in db: # Check if user is in Db 
        if user.id == user_id: # If IDs match 
            if user_update.f_name is not None: # If the user updates the f_name should not be none
                user.f_name = user_update.f_name
            if user_update.l_name is not None:
                user.l_name = user_update.l_name # If the user updates the l_name should not be none
            if user_update.m_name is not None:
                user.m_name = user_update.m_name # If the user updates the m_name should not be none
            if user_update.roles is not None: # If the user updates the role should not be none
                user.roles = user_update.roles
            return 
    raise HTTPException( # This is the error message if the user is not found
        status_code=404,
        detail=f"user with id {user_id} does not exist"
        )

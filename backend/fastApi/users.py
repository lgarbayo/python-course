from http.client import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str

users_list = [User(id=1, name="John Doe"),
        User(id=2, name="Jane Doe")]

@app.get("/usersjson")
async def users_json():
    return [{"id": 1, "name": "John Doe"}, 
            {"id": 2, "name": "Jane Doe"},
            {"id": 3, "name": "Jim Beam"},
            {"id": 4, "name": "Jack Daniels"}]

@app.get("/users")
async def users():
    return users_list

#path
@app.get("/user/{id}")
async def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No user found"}
    
#query
@app.get("/user/")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No user found"}
    
@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="User already exists")
    users_list.append(user)
    return user

@app.put("/user/")
async def user(user: User):
    found = False
    for i, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[i] = user
            found = True
    if not found:
        return {"error": "User not found"}
    return user

@app.delete("/user/{id}")
async def user(id: int):
    found = False
    for i, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[i]
            found = True
            return {"message": "User deleted"}
    if not found:
        return {"error": "User not found"}

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No user found"}
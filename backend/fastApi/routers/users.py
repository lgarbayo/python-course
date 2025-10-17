from http.client import HTTPException
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404: {"message": "Not found"}})

class User(BaseModel):
    id: int
    name: str

users_list = [User(id=1, name="John Doe"),
        User(id=2, name="Jane Doe")]

@router.get("/json")
async def users_json():
    return [{"id": 1, "name": "John Doe"}, 
            {"id": 2, "name": "Jane Doe"},
            {"id": 3, "name": "Jim Beam"},
            {"id": 4, "name": "Jack Daniels"}]

@router.get("/")
async def users():
    return users_list

#path
@router.get("/{id}")
async def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No user found"}
    
#query
@router.get("/")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No user found"}
    
@router.post("/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="User already exists")
    users_list.routerend(user)
    return user

@router.put("/")
async def user(user: User):
    found = False
    for i, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[i] = user
            found = True
    if not found:
        return {"error": "User not found"}
    return user

@router.delete("/{id}")
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
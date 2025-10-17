from fastapi import FastAPI
from routers import products
from routers import users

app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return "Hola Mundo!"

@app.get("/git")
async def git():
    return {"url": "https://github.com/lgarbayo"}
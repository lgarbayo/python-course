from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola Mundo!"

@app.get("/git")
async def git():
    return {"url": "https://github.com/lgarbayo"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
async def get_products():
    return [{"id": 1, "name": "Product 1"}, {"id": 2, "name": "Product 2"}]
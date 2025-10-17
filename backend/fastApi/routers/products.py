from fastapi import APIRouter

router = APIRouter(prefix="/products",
                    tags=["products"],
                   responses={404: {"message": "Not found"}})

products_list = [{"id": 1, "name": "Product 1"},
                    {"id": 2, "name": "Product 2"}]

@router.get("/")
async def get_products():
    return products_list

@router.get("/{id}")
async def get_products(id: int):
    return products_list[id]


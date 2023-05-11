from fastapi import APIRouter
from typing import Optional
from fastapi import Query


#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/products",
    tags=["Product"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_root():
    return [{"id":1,"product": "Laptop"}, {"id":2,"product": "Mobile"}]


@router.get("/{product_id}")
async def read_item(product_id: int):
    return {"id": product_id, "name": "Mobile", "code": "M12", "price": 200.0}


@router.get("/detail")
async def read_item_detail(q: Optional[str] = Query(None, max_length=50)):
    results = {"products": [{"id": 1}, {"id": 2}]}
    if q:
        results.update({"q": q})
    return results


@router.delete("/{product_id}/delete")
async def delete_item(product_id: int):
    return {"id": product_id, "is_deleted": True}

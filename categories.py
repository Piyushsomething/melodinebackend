from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from typing import List
from helpers import all_data,save_data

class Category(BaseModel):
    name: str
    img: str
    route: str


categories_router = APIRouter()

# # Sample initial data
# initial_categories = [
#     {"name": "Rock", "img": "/images/genre/rock.PNG", "route": "#"},
#     {"name": "Pop", "img": "/images/genre/pop.PNG", "route": "#"},
#     {"name": "Jazz", "img": "/images/genre/jazz.PNG", "route": "#"},
#     {"name": "Disco", "img": "/images/genre/disco.PNG", "route": "#"},
# ]

initial_categories = all_data["initial_categories"]
categories = [data for data in initial_categories]


@categories_router.get("/categories", response_model=List[Category])
async def read_categories():
    return categories

# @categories_router.get("/categories/{category_name}", response_model=Category)
# async def read_category(category_name: str):
#     try:
#         return next(category for category in categories if category.name == category_name)
#     except StopIteration:
#         raise HTTPException(status_code=404, detail="Category not found")

@categories_router.post("/categories", response_model=Category)
async def create_category(category: Category):
    categories.append(category)
    all_data["initial_categories"] = categories
    save_data(all_data)
    return category

@categories_router.put("/categories/{category_name}", response_model=Category)
async def update_category(category_name: str, updated_category: Category):
    try:
        index = next(i for i, category in enumerate(categories) if category["name"] == category_name)
        categories[index] = updated_category.dict()
        all_data["initial_categories"][index] = categories
        save_data(all_data)
        return updated_category
    except StopIteration:
        raise HTTPException(status_code=404, detail="Category not found")

@categories_router.delete("/categories/{category_name}")
async def delete_category(category_name: str):
    try:
        # print((categories), type(categories[0]))
        index = next(i for i, category in enumerate(categories) if category["name"] == category_name)
        del categories[index]
        del all_data["initial_categories"][index]
        save_data(all_data)
        return {"message": "Category deleted successfully"}
    except StopIteration:
        raise HTTPException(status_code=404, detail="Category not found")

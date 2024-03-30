from fastapi import  APIRouter
from pydantic import BaseModel
from typing import List, Optional
from helpers import all_data, save_data
# from fastapi.responses import JSONResponse

about_router = APIRouter()

class AboutData(BaseModel):
    title: str
    paragraphs: List[str]
    image: Optional[str]

# # Sample initial data
# initial_about_data = {
#     "title": "About Melodine Records",
#     "paragraphs": [
#         "Where the rhythm of life meets the harmony of dreams. Founded in 2024, Melodine Records emerges as a beacon for aspiring artists and producers, a sanctuary where talent meets opportunity.",
#         "At Melodine Records, our mission is simple yet profound: to provide a nurturing platform for artists to amplify their voices and for producers to sculpt their sonic landscapes. We are not just a record label; we are a catalyst for artistic evolution, a conduit through which melodies flow and dreams take flight.",
#         "Our ethos is rooted in a deep-seated passion for music in all its forms. We believe in the power of melody to transcend boundaries, to uplift spirits, and to soundtrack the moments that define our lives. Whether you're seeking solace in a soulful ballad or igniting the dance floor with infectious beats, Melodine Records is here to accompany you through every mood and occasion.",
#         "But our journey is not one we embark upon alone. We recognize that our success is intertwined with the support and enthusiasm of our community. That's why we call upon you, music lovers and dream chasers alike, to join us on this exhilarating voyage. Together, let us cultivate a rich tapestry of sound, weaving together diverse voices and genres to create something truly extraordinary.",
#         "So, whether you're an artist looking for a platform to shine or a music aficionado eager to discover your next favorite tune, Melodine Records welcomes you with open arms. Let's write the next chapter in the symphony of our lives, one melody at a time. Thank you for your support as we embark on this thrilling adventure together."
#     ],
#     "image": "https://i.imgur.com/WbQnbas.png"
# }

# about_data = AboutData(**initial_about_data)
# about_data = all_data["initial_about_data"]

@about_router.get("/about", response_model=AboutData)
async def read_about_data():
    return all_data.get("initial_about_data", [])

@about_router.put("/about", response_model=AboutData)
async def update_about_data(updated_data: AboutData):
    # print(all_data["initial_about_data"]["title"])
    all_data["initial_about_data"]["title"] = updated_data.title
    all_data["initial_about_data"]["paragraphs"] = updated_data.paragraphs
    all_data["initial_about_data"]["image"] = updated_data.image
    save_data(all_data)
    return all_data["initial_about_data"]

# @about_router.delete("/about")
# async def delete_about_data():
#     all_data["initial_about_data"] = None
#     save_data(all_data)
#     return {"message": "Data deleted successfully"}

@about_router.post("/about", response_model=AboutData)
async def create_about_data(new_data: AboutData):
    all_data["initial_about_data"] = new_data.dict()
    save_data(all_data) 
    return all_data["initial_about_data"]
    # return JSONResponse(content={"message": "Data created successfully", "AboutPage":new_data.dict()},status_code=201)

from fastapi import FastAPI
import uvicorn
from categories import categories_router
from songs import songs_router
from about import about_router
from artist import artists_router
from popularsongs import popular_songs_router
from helpers import all_data

app = FastAPI()
app.include_router(categories_router, prefix="/api")
app.include_router(songs_router, prefix="/api")
app.include_router(about_router, prefix="/api")
app.include_router(artists_router, prefix="/api")
app.include_router(popular_songs_router, prefix="/api")

@app.get("/api/alldata")
async def root():
    return all_data

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)


##**********************************************************************

# from pydantic import BaseModel, HttpUrl
# from typing import List
# from fastapi import UploadFile
# from fastapi import FastAPI, File, UploadFile


# app = FastAPI()

# class AboutData(BaseModel):
#     title: str
#     paragraphs: List[str]
#     image: UploadFile


# @app.post("/upload/")
# async def upload_image(about_data: AboutData):
#     # Save the uploaded image file
#     with open(f"uploaded_images/{about_data.image.filename}", "wb") as buffer:
#         buffer.write(await about_data.image.read())
    
#     return {"filename": about_data.image.filename}

#*************************************************************************
#TODO : Uploading image file
#TODO : How api change frontend code
#TODO : Find free hosting 
#TODO : Upgrade to form submission instead of json
from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from categories import categories_router
from songs import songs_router
from about import about_router
from artist import artists_router
from popularsongs import popular_songs_router

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this based on your requirements
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(categories_router, prefix="/api")
app.include_router(songs_router, prefix="/api")
app.include_router(about_router, prefix="/api")
app.include_router(artists_router, prefix="/api")
app.include_router(popular_songs_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hello from MelonI backend!"}

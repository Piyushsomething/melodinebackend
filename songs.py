from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from typing import List

songs_router = APIRouter()


class Song(BaseModel):
    id: int
    title: str
    artist: str
    duration: str


initial_songs = [
    {"id": 1, "title": "Light Comes Up", "artist": "Bayza", "duration": "02:49"},
    {"id": 2, "title": "On Your Mind", "artist": "Bayza", "duration": "02:33"},
    {"id": 3, "title": "Everything I Wanted", "artist": "Billie Eilish", "duration": "04:12"},
    {"id": 4, "title": "Young & Free", "artist": "Bayza", "duration": "03:23"},
    {"id": 5, "title": "Solace", "artist": "Bayza", "duration": "03:52"},
    # Add more sample songs as needed
]

songs = [Song(**data) for data in initial_songs]

@songs_router.get("/songs", response_model=List[Song])
async def read_songs():
    return songs

@songs_router.get("/songs/{song_id}", response_model=Song)
async def read_song(song_id: int):
    try:
        return next(song for song in songs if song.id == song_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail="Song not found")

@songs_router.post("/songs", response_model=Song)
async def create_song(song: Song):
    songs.append(song)
    return song

@songs_router.put("/songs/{song_id}", response_model=Song)
async def update_song(song_id: int, updated_song: Song):
    try:
        index = next(i for i, song in enumerate(songs) if song.id == song_id)
        songs[index] = updated_song
        return updated_song
    except StopIteration:
        raise HTTPException(status_code=404, detail="Song not found")

@songs_router.delete("/songs/{song_id}")
async def delete_song(song_id: int):
    try:
        index = next(i for i, song in enumerate(songs) if song.id == song_id)
        del songs[index]
        return {"message": "Song deleted successfully"}
    except StopIteration:
        raise HTTPException(status_code=404, detail="Song not found")

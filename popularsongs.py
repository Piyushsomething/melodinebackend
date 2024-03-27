from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List



popular_songs_router = APIRouter()


class PopularSong(BaseModel):
    id: int
    title: str
    artist: str
    duration: str



# Sample initial popular release songs data
initial_popular_release_songs = [
    {"id": 1, "title": "Light Comes Up", "artist": "Bayza", "duration": "02:49"},
    {"id": 2, "title": "On Your Mind", "artist": "NEW", "duration": "02:33"},
    {"id": 3, "title": "Everything I Wanted", "artist": "Billie Eilish", "duration": "04:12"},
    {"id": 4, "title": "Young & Free", "artist": "Bayza", "duration": "03:23"},
    # Add the rest of your songs here
]

popular_release_songs = [PopularSong(**song) for song in initial_popular_release_songs]



@popular_songs_router.get("/songs", response_model=List[PopularSong])
async def read_songs():
    return popular_release_songs

@popular_songs_router.get("/songs/{song_id}", response_model=PopularSong)
async def read_song(song_id: int):
    song = next((song for song in popular_release_songs if song.id == song_id), None)
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return song

@popular_songs_router.post("/songs", response_model=PopularSong)
async def create_song(song: PopularSong):
    popular_release_songs.append(song)
    return song

@popular_songs_router.put("/songs/{song_id}", response_model=PopularSong)
async def update_song(song_id: int, updated_song: PopularSong):
    for i, song in enumerate(popular_release_songs):
        if song.id == song_id:
            popular_release_songs[i] = updated_song
            return updated_song
    raise HTTPException(status_code=404, detail="Song not found")

@popular_songs_router.delete("/songs/{song_id}")
async def delete_song(song_id: int):
    global popular_release_songs
    popular_release_songs = [song for song in popular_release_songs if song.id != song_id]
    return {"message": "Song deleted successfully"}



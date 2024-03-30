from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from helpers import all_data, save_data


popular_songs_router = APIRouter()


class PopularSong(BaseModel):
    id: int
    title: str
    artist: str
    duration: str



# # Sample initial popular release songs data
# initial_popular_release_songs = [
#     {"id": 1, "title": "Light Comes Up", "artist": "Bayza", "duration": "02:49"},
#     {"id": 2, "title": "On Your Mind", "artist": "NEW", "duration": "02:33"},
#     {"id": 3, "title": "Everything I Wanted", "artist": "Billie Eilish", "duration": "04:12"},
#     {"id": 4, "title": "Young & Free", "artist": "Bayza", "duration": "03:23"},
#     # Add the rest of your songs here
# ]

initial_popular_release_songs= all_data["initial_popular_release_songs"]
popular_release_songs = [song for song in initial_popular_release_songs]



@popular_songs_router.get("/popularsongs", response_model=List[PopularSong])
async def read_songs():
    return popular_release_songs

@popular_songs_router.get("/popularsongs/{song_id}" )#response_model=PopularSong
async def read_song(song_id: int):
    # song = next((song for song in popular_release_songs if song.id == song_id), None)
    psong = popular_release_songs[song_id-1]
    if psong is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return psong

@popular_songs_router.post("/popularsongs", response_model=PopularSong)
async def create_song(song: PopularSong):
    popular_release_songs.append(song.dict())
    all_data["initial_popular_release_songs"] = popular_release_songs
    save_data(all_data)
    return song

@popular_songs_router.put("/popularsongs/{song_id}", response_model=PopularSong)
async def update_song(song_id: int, updated_song: PopularSong):
    try:
        popular_release_songs[song_id-1] = updated_song.dict()
        all_data["initial_popular_release_songs"][song_id-1] = updated_song.dict()
        save_data(all_data)
        return updated_song
    except KeyError:
        raise HTTPException(status_code=404, detail="Song not found")

@popular_songs_router.delete("/popularsongs/{song_id}")
async def delete_song(song_id: int):
    try:
        del popular_release_songs[song_id - 1]  # Adjusting for 1-based indexing
        del all_data["initial_popular_release_songs"][song_id - 1]
        save_data(all_data)
        return {"message": "Song deleted successfully"}
    except KeyError:
        raise HTTPException(status_code=404, detail="Song not found")




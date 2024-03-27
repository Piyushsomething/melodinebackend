from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from typing import List, Optional

artists_router = APIRouter()


class Artist(BaseModel):
    name: str
    bio: str
    songs: List[dict]
    spotifyLink: Optional[str]
    youtubeLink: Optional[str]
    wikipediaLink: Optional[str]
    appleMusicLink: Optional[str]
    profileIcon: Optional[str]



initial_artists = [
    {
        "name": "Artist 1",
        "bio": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam quis ante et elit convallis scelerisque. Sed ac ante sit amet ipsum fringilla tincidunt.",
        "songs": [
            {"name": "Song A", "length": "3:45", "info": "Lorem ipsum dolor sit amet."},
            {"name": "Song B", "length": "4:20", "info": "Sed do eiusmod tempor incididunt."},
            {"name": "Song C", "length": "2:55", "info": "Ut enim ad minim veniam."},
            {"name": "Song D", "length": "5:10", "info": "Duis aute irure dolor in reprehenderit."},
            {"name": "Song E", "length": "3:30", "info": "Excepteur sint occaecat cupidatat non proident."}
        ],
        "spotifyLink": "https://open.spotify.com",
        "youtubeLink": "https://www.youtube.com",
        "wikipediaLink": "https://www.wikipedia.org",
        "appleMusicLink": "https://music.apple.com",
        "profileIcon": "https://via.placeholder.com/150"
    },
    {
        "name": "Artist 2",
        "bio": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam quis ante et elit convallis scelerisque. Sed ac ante sit amet ipsum fringilla tincidunt.",
        "songs": [
            {"name": "Song X", "length": "4:00", "info": "Lorem ipsum dolor sit amet."},
            {"name": "Song Y", "length": "3:15", "info": "Sed do eiusmod tempor incididunt."},
            {"name": "Song Z", "length": "3:45", "info": "Ut enim ad minim veniam."}
        ],
        "spotifyLink": "https://open.spotify.com",
        "youtubeLink": "https://www.youtube.com",
        "wikipediaLink": "https://www.wikipedia.org",
        "appleMusicLink": "https://music.apple.com",
        "profileIcon": "https://via.placeholder.com/150"
    }
]


artists = [Artist(**data) for data in initial_artists]



@artists_router.get("/artists", response_model=List[Artist])
async def read_artists():
    return artists

@artists_router.get("/artists/{artist_id}", response_model=Artist)
async def read_artist(artist_id: int):
    try:
        return artists[artist_id - 1]  # Adjusting for 1-based indexing
    except IndexError:
        raise HTTPException(status_code=404, detail="Artist not found")

@artists_router.post("/artists", response_model=Artist)
async def create_artist(artist: Artist):
    artists.append(artist)
    return artist

@artists_router.put("/artists/{artist_id}", response_model=Artist)
async def update_artist(artist_id: int, updated_artist: Artist):
    try:
        artists[artist_id - 1] = updated_artist  # Adjusting for 1-based indexing
        return updated_artist
    except IndexError:
        raise HTTPException(status_code=404, detail="Artist not found")

@artists_router.delete("/artists/{artist_id}")
async def delete_artist(artist_id: int):
    try:
        del artists[artist_id - 1]  # Adjusting for 1-based indexing
        return {"message": "Artist deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Artist not found")

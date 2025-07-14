from fastapi import APIRouter, Depends, HTTPException, Header
from app.services.swapi_client import SWAPIClient
from slowapi.util import get_remote_address
from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address)


def api_key_auth(x_api_key: str = Header(...)):
    if x_api_key != "your-secret-key":
        raise HTTPException(status_code=401, detail="Invalid API Key")


router = APIRouter(dependencies=[Depends(api_key_auth)])
swapi_client = SWAPIClient()


@router.get("/movies")
@limiter.limit("5/minute")
async def get_movies():
    return await swapi_client.get_movies()


@router.get("/characters")
@limiter.limit("5/minute")
async def get_characters():
    return await swapi_client.get_people()


@router.get("/planets")
@limiter.limit("5/minute")
async def get_planets():
    return await swapi_client.get_planets()


@router.get("/ships")
@limiter.limit("5/minute")
async def get_ships():
    return await swapi_client.get_starships()


@router.get("/filter/movies")
@limiter.limit("5/minute")
async def filter_movies(year: int = None, title: str = None):
    movies = await swapi_client.get_movies()
    if year:
        movies = [
            movie for movie in movies if movie["release_date"].startswith(str(year))
        ]
    if title:
        movies = [movie for movie in movies if title.lower() in movie["title"].lower()]
    return movies


@router.get("/sort/characters")
@limiter.limit("5/minute")
async def sort_characters(sort_by: str = "name"):
    characters = await swapi_client.get_people()
    return sorted(characters, key=lambda x: x[sort_by])

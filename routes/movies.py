from fastapi import APIRouter
from config.db import client_atlas
from schemas.movie import movieEntity, moviesEntity

movies = APIRouter()

@movies.get("/movies")
def get_movie():
    return movieEntity(client_atlas.pi_henry.movies.find_one({}))



@movies.get("/movies_per_day/{day}")
def retrieve_movies_per_day():
    return "Hello"
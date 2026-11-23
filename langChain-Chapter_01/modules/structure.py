from pydantic import BaseModel, Field

class LLMResponseStructure(BaseModel):
    name: str = Field(description="Name of the person")
    email: str = Field(description="Email address of the person")
    age: int = Field(description="Age of the person")
    profession: str = Field(description="Profession of the person")
    friends: list = Field(description="List of friends of the person")

class MovieResponseStructure(BaseModel):
    title: str = Field(description="Title of the movie")
    cast: str = Field(description="Cast of the movie")
    year: int = Field(description="Release year of the movie")
    genre: str = Field(description="Genre of the movie")

class MoviesResponseStructure(BaseModel):
    movies: list[MovieResponseStructure] = Field(description="List of movies with their details")
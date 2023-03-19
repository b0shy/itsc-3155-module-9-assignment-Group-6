# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository


def test_get_movie_by_title():

    movies = get_movie_repository()

    movies.create_movie("Big Daddy", "Dennis Dugan", 5)
    movies.create_movie("Titanic", "James Cameron", 4)
    movies.create_movie("Cruising", "William Friedkin", 5)

    searched_movie = movies.get_movie_by_title("Big Daddy")
    searched_movie2 = movies.get_movie_by_title("Titanic")
    searched_movie3 = movies.get_movie_by_title("Cruising")

    assert searched_movie.title == "Big Daddy"
    assert searched_movie.director == "Dennis Dugan"
    assert searched_movie.rating == 5

    assert searched_movie2.title == "Titanic"
    assert searched_movie2.director == "James Cameron"
    assert searched_movie2.rating == 4

    assert searched_movie3.title == "Cruising"
    assert searched_movie3.director == "William Friedkin"
    assert searched_movie3.rating == 5

# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie


def test_create_movie():
    _movie_repo= get_movie_repository()
    movie = _movie_repo.create_movie('Jurrasic Park', 'Steven Spielberg', 4)
    assert movie.title == 'Jurrasic Park'
    assert movie.director == 'Steven Spielberg'
    assert movie.rating == 4
    assert type(movie) == Movie
    assert _movie_repo.get_movie_by_title('Jurrasic Park') != None
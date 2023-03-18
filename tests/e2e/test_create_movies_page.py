# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_create_movies(test_app):
    _movie_repo= get_movie_repository()
    dict = {'title': 'Jurrasic Park','director': 'Steven Spielberg','rating': '4'}
    response = test_app.post('/movies', data=dict)
    assert _movie_repo.get_movie_by_title('Jurrasic Park')!=None
    assert response.request.path == "/movies"
    assert response.status_code == 302
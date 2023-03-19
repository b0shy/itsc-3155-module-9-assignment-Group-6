# was made with the help of chatgpt

# TODO: Feature 3
from app import app, movie_repository


def test_search_movies():

    test_app = app.test_client()
    movie_repository.create_movie("The Matrix", "Lilly Wachowski", 5)
    # Test searching for a movie that exists
    response = test_app.get('/movies/search?title=The+Matrix')
    assert response.status_code == 200
    assert b'<td>The Matrix</td>' in response.data
    assert b'<td>5</td>' in response.data

    # Test searching for a movie that does not exist
    response = test_app = app.test_client().get(
        '/movies/search?title=Nonexistent+Movie')
    assert response.status_code == 200
    assert b'<td>The Matrix</td>' not in response.data
    assert b'<td>5</td>' not in response.data

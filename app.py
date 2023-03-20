from flask import Flask, redirect, render_template,request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    # I used chatGPT to learn how to use the function and its output inside my list all movies html template
    movie=movie_repository.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, movies=movie)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    title = request.form['title']
    director = request.form['director']
    rating = int(request.form['rating'])
    movie_repository.create_movie(title, director, rating)
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    title = request.args.get('title')
    searched_movie = movie_repository.get_movie_by_title(title)
    return render_template('search_movies.html', search_active=True, searched_movie=searched_movie)

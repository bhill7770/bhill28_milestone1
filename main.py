import flask 
import json
import requests
import os 

app = flask.Flask(__name__)

BASE_URL = "https://api.themoviedb.org/3"

top_films = requests.get(f"{BASE_URL}/discover/movie", params={'api_key': os.getenv("API_KEY")})
data = top_films.json()

for pop_movie in data["results"]:
    Movie_title = pop_movie['title']
    brief_summary = pop_movie['overview']
    Release_date = pop_movie['release_date']
    rating = pop_movie['vote_average']
    genres = pop_movie['genre_ids']
    movie_image = pop_movie['poster_path']

  
@app.route("/")

def index():

    return flask.render_template("index.html", data = data)

if __name__ ==  "__main__":
    app.run(use_reloader = True, debug=True)

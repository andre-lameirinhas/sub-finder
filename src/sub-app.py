from flask import Flask
import interactor

app = Flask(__name__)


@app.route('/movie/<movie_name>')
def movie(movie_name: str):
    interactor.get_movie_subtitles(
        movie_name=movie_name
    )
    return "Success", 200


@app.route('/episode/<series_name>/<season_number>/<episode_number>')
def episode(series_name: str, season_number: int, episode_number: int):
    interactor.get_episode_subtitles(
        series_name=series_name,
        season_number=season_number,
        episode_number=episode_number
    )
    return "Success", 200


if __name__ == '__main__':
    app.run(debug=True)

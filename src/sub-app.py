from flask import Flask, request
import interactor

app = Flask(__name__)


@app.route('/movie/<movie_name>')
def movie(movie_name: str):

    year = request.args.get('year', default=None, type=int)

    interactor.get_movie_subtitles(
        movie_name=movie_name,
        year=year
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

from argparse import ArgumentParser
import constants as cts
import interactor
import logging

parser = ArgumentParser(description="Subtitles Finder")
parser.add_argument("-t", "--type", metavar="type", type=str,
                    choices=["movie", "episode", "season"], default="movie", help="resource type")
parser.add_argument("-s", "--season", metavar="season",
                    type=int, help="intended season")
parser.add_argument("-e", "--episode", metavar="episode",
                    type=int, help="intended episode")
parser.add_argument("-l", "--language", metavar="lang",
                    type=str, default="en", help="subtitle language")
parser.add_argument("-y", "--year", metavar="year",
                    type=int, help="resource release year")
parser.add_argument("resource_name", type=str,
                    help="resource that needs subtitles")
args = parser.parse_args()

logging.basicConfig(
    level=cts.LOG_LEVEL.upper(),
    format=cts.LOG_FORMAT
)

resource_type = args.type

if resource_type == "movie":
    interactor.get_movie_subtitles(
        movie_name=args.resource_name,
        language=args.language,
        year=args.year
    )
elif resource_type == "episode":
    interactor.get_episode_subtitles(
        series_name=args.resource_name,
        season_number=args.season,
        episode_number=args.episode,
        language=args.language
    )
else:
    logging.error(f"Invalid resource_type: {resource_type}")
    exit(1)

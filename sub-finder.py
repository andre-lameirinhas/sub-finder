from argparse import ArgumentParser
import gateway as gw
import constants as cts
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
parser.add_argument("resource_name", type=str,
                    help="resource that needs subtitles")
args = parser.parse_args()

logging.basicConfig(
    level=cts.LOG_LEVEL.upper(),
    format=cts.LOG_FORMAT
)

resource_type = args.type

search_params = {
    "query": args.resource_name,
    "languages": args.language,
    "type": resource_type,
    "order_by": "download_count"
}

if resource_type == "episode":
    search_params.update({
        "season_number": args.season,
        "episode_number": args.episode
    })

search_results = gw.search_subtitles(search_params)

if search_results["total_count"] == 0:
    logging.info("No subtitles found")
    exit()

gw.login()

first_result = search_results["data"][0]
file_data = first_result["attributes"]["files"][0]

file_id = file_data["file_id"]
file_name = file_data["file_name"]

download_body = {
    "file_id": file_id,
    "sub_format": "srt",
    "file_name": file_name
}

subtitles = gw.download_subtitles(download_body)

# gw.logout()

logging.info(f"Writing subtitles to file {file_name}")
with open(file_name, "w", encoding="utf-8") as sub_file:
    sub_file.write(subtitles)

logging.info("Process finished successfully")

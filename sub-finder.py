from argparse import ArgumentParser
import gateway as gw
import constants as cts
import logging

parser = ArgumentParser(description="Subtitles Finder")
parser.add_argument("movie_name", type=str, help="movie that needs subtitles")
parser.add_argument("-l", "--language", metavar="lang",
                    type=str, default="en", help="subtitle language")
args = parser.parse_args()

logging.basicConfig(
    level=cts.LOG_LEVEL.upper(),
    format=cts.LOG_FORMAT
)

search_params = {
    "query": args.movie_name,
    "languages": args.language,
    "type": "movie",
    # "order_by": "download_count"
}

result = gw.search_subtitles(search_params)

if result["total_count"] == 0:
    logging.info("No subtitles found")
    exit()

file_data = result["data"][0]["attributes"]["files"][0]

gw.login()

download_body = {
    "file_id": file_data["file_id"],
    "sub_format": "srt",
    "file_name": file_data["file_name"].removesuffix(".srt")
}

sub_metadata = gw.download_subtitles_metadata(download_body)

filename = sub_metadata["file_name"]

sub = gw.download_from_url(sub_metadata["link"])

logging.info(f"Writing subtitles to file {filename}")
with open(filename, "w", encoding="utf-8") as sub_file:
    sub_file.write(sub.text)

logging.info("Process finished successfully")

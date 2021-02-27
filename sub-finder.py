import argparse
import gateway as gw

parser = argparse.ArgumentParser(description="Subtitles Finder")
parser.add_argument("movie_name", type=str, help="Movie that needs subtitles")
parser.add_argument("-l", "--language", metavar="lang", type=str, default="en", help="Subtitle language")
args = parser.parse_args()

search_params = {
    "query": args.movie_name,
    "languages": args.language,
    "type": "movie",
    "order_by": "download_count"
}

print("Searching for available subtitles")
result = gw.search_subtitles(search_params)

if result["total_count"] == 0:
    exit("No subtitles found")

file_data = result["data"][0]["attributes"]["files"][0]

print("Obtaining token")
token = gw.login()["token"]

download_body = {
    "file_id": file_data["file_id"],
    "sub_format": "srt",
    "file_name": file_data["file_name"].removesuffix(".srt")
}

print("Downloading subtitles metadata")
sub_metadata = gw.download_subtitles_metadata(download_body, token)

print("Downloading subtitles")
sub = gw.download_from_url(sub_metadata["link"])

with open(sub_metadata["file_name"], "w", encoding="utf-8") as sub_file:
    sub_file.write(sub.text)
import gateway as gw
import logging


def get_movie_subtitles(movie_name: str, language="en"):
    search_params = {
        "query": movie_name,
        "languages": language,
        "type": "movie",
        "order_by": "download_count"
    }

    get_subtitles(search_params)


def get_episode_subtitles(series_name: str, season_number: int, episode_number, language="en"):
    search_params = {
        "query": series_name,
        "season_number": season_number,
        "episode_number": episode_number,
        "languages": language,
        "type": "episode",
        "order_by": "download_count"
    }

    get_subtitles(search_params)


def get_subtitles(search_params: dict):
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

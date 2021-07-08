import gateway as gw
import logging


def get_movie_subtitles(movie_name: str, language="en"):
    search_params = {
        "query": movie_name,
        "languages": language,
        "type": "movie",
        # "order_by": "download_count"
    }

    feature = gw.search_features(search_params)["data"][0]

    feature_id = feature["id"]
    feature_title = feature["attributes"]["title"]

    subtitles_count = feature["attributes"]["subtitles_counts"][language]

    if subtitles_count == 0:
        logging.info("No subtitles found")
        exit()

    search_params.pop("query")
    search_params.update({
        "id": feature_id
    })

    get_subtitles(search_params, feature_title)


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


def get_subtitles(search_params: dict, title="No title"):
    search_results = gw.search_subtitles(search_params)

    if search_results["total_count"] == 0:
        logging.info("No subtitles found")
        exit()

    gw.login()

    first_result = search_results["data"][0]
    file_data = first_result["attributes"]["files"][0]

    file_id = file_data["file_id"]
    file_name = file_data["file_name"] if file_data["file_name"] is not None else title

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

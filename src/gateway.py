from requests import Session
import constants as cts
import logging

session = Session()
session.headers.update({
    "Api-Key": cts.API_KEY
})


def login():
    logging.info(f"Logging in with user {cts.USERNAME}")

    res = session.post(
        url=cts.OPEN_SUBTITLES_URL + cts.LOGIN_ENDPOINT,
        headers={"Content-Type": "multipart/form-data"},
        data={
            "username": cts.USERNAME,
            "password": cts.PASSWORD
        }
    )

    res.raise_for_status()

    token = res.json()["token"]

    session.headers.update({
        "Authorization": f"Bearer {token}"
    })

# TODO Find out why logout does not logout


def logout():
    logging.info(f"Logging out with user {cts.USERNAME}")

    res = session.delete(
        url=cts.OPEN_SUBTITLES_URL + cts.LOGOUT_ENDPOINT
    )

    res.raise_for_status()


def search_subtitles(params: dict):
    logging.info(f"Searching for subtitles with params {params}")

    res = session.get(
        url=cts.OPEN_SUBTITLES_URL + cts.SUBTITLES_ENDPOINT,
        params=params
    )
    res.raise_for_status()

    return res.json()


def search_features(params: dict):
    logging.info(f"Searching for feature with params {params}")

    res = session.get(
        url=cts.OPEN_SUBTITLES_URL + cts.FEAURES_ENDPOINT,
        params=params
    )
    res.raise_for_status()

    return res.json()


def download_subtitles(body: dict):
    logging.info(f"Downloading subtitles metadata with body {body}")

    metadata_response = session.post(
        url=cts.OPEN_SUBTITLES_URL + cts.DOWNLOAD_ENDPOINT,
        headers={"Content-Type": "multipart/form-data"},
        data=body
    )

    metadata_response.raise_for_status()

    download_link = metadata_response.json()["link"]

    logging.info("Downloading subtitles from URL")

    subtitle_response = session.get(download_link)

    subtitle_response.raise_for_status()

    return subtitle_response.text

from requests import Session
import constants as cts
from utils import ident_json
import logging

session = Session()
session.headers.update({
    "Api-Key": cts.API_KEY
})


def login():
    logging.info(f"Logging in with user {cts.USERNAME}")
    headers = {
        "Content-Type": "multipart/form-data"
    }

    body = {
        "username": cts.USERNAME,
        "password": cts.PASSWORD
    }

    res = session.post(
        url=cts.OPEN_SUBTITLES_URL + cts.LOGIN_ENDPOINT,
        headers=headers,
        data=body
    )

    res.raise_for_status()

    token = res.json()["token"]
    session.headers.update({
        "Authorization": f"Bearer {token}"
    })


def search_subtitles(params: dict):
    logging.info(f"Searching for subtitles with params {params}")

    res = session.get(
        url=cts.OPEN_SUBTITLES_URL + cts.SUBTITLES_ENDPOINT,
        params=params
    )
    res.raise_for_status()

    return res.json()


def download_subtitles_metadata(body: dict):
    logging.info(f"Downloading subtitles metadata with body {body}")

    headers = {
        "Content-Type": "multipart/form-data"
    }

    res = session.post(
        url=cts.OPEN_SUBTITLES_URL + cts.DOWNLOAD_ENDPOINT,
        headers=headers,
        data=body
    )

    res.raise_for_status()

    return res.json()


def download_from_url(url: str):
    logging.info("Downloading subtitles from URL")

    res = session.get(url)

    res.raise_for_status()

    return res

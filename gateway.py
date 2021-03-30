import requests
from requests import Request
import constants as cts
import utils

session = requests.Session()
session.headers.update({
    "Api-Key": cts.API_KEY
})

def login():

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
    print("request headers")
    utils.print_json(res.request.headers)
    #print("response header")
    #utils.print_json(res.headers)

    print("response body")
    utils.print_json(res.json())

    res.raise_for_status()

    token = res.json()["token"]
    session.headers.update({
        "Authorization": f"Bearer {token}"
    })

def search_subtitles(params: dict):

    res = session.get(
        url=cts.OPEN_SUBTITLES_URL + cts.SUBTITLES_ENDPOINT,
        params=params
    )

    res.raise_for_status()
    return res.json()


def download_subtitles_metadata(body: dict):

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
    res = session.get(url)

    res.raise_for_status()
    return res

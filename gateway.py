import requests
import constants as cts

def login():

    headers = {
        "Api-Key": cts.API_KEY,
        "Content-Type": "multipart/form-data"
    }

    body = {
        "username": cts.USERNAME,
        "password": cts.PASSWORD
    }

    res = requests.post(
        url = cts.OPEN_SUBTITLES_URL + cts.LOGIN_ENDPOINT,
        headers = headers,
        data = body
    )

    res.raise_for_status()
    return res.json()

def search_subtitles(params: dict):

    headers = {
        "Api-Key": cts.API_KEY
    }

    res = requests.get(
        url = cts.OPEN_SUBTITLES_URL + cts.SUBTITLES_ENDPOINT,
        params = params,
        headers = headers
    )

    res.raise_for_status()
    return res.json()

def download_subtitles_metadata(body: dict, token: str):

    headers = {
        "Api-Key": cts.API_KEY,
        "Content-Type": "multipart/form-data",
        "Authorization": f"Bearer {token}"
    }

    res = requests.post(
        url = cts.OPEN_SUBTITLES_URL + cts.DOWNLOAD_ENDPOINT,
        headers = headers,
        data = body
    )

    res.raise_for_status()
    return res.json()

def download_from_url(url: str):
    res = requests.get(url)

    res.raise_for_status()
    return res

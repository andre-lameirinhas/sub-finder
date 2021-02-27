import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = "5vA2m4IssF1LjW0EiqIEyTGszRfEXQxI"

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

OPEN_SUBTITLES_URL = "https://www.opensubtitles.com"

# Endpoints
SUBTITLES_ENDPOINT = "/api/v1/subtitles"
LOGIN_ENDPOINT = "/api/v1/login"
DOWNLOAD_ENDPOINT = "/api/v1/download"
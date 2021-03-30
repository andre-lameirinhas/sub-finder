import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.getenv('API_KEY')

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

LOG_LEVEL = os.getenv('LOG_LEVEL')

OPEN_SUBTITLES_URL = "https://www.opensubtitles.com"

# Endpoints
SUBTITLES_ENDPOINT = "/api/v1/subtitles"
LOGIN_ENDPOINT = "/api/v1/login"
DOWNLOAD_ENDPOINT = "/api/v1/download"

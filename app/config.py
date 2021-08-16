import secrets


class Config:
    # api name
    NAME = "api-hub"

    SECRET_KEY = secrets.token_hex(8)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # links
    POSTMAN_COLLECTION_URL = (
        "https://www.getpostman.com/collections/87ab6adecba171c3525c"
    )
    GITHUB_REPO_URL = "https://github.com/rrkas/api-hub"
    LOCALHOST_URL = "http://127.0.0.1:5000/"

    # home
    CREATOR = "Rohnak Agarwal"
    VERSION = "1.0.0"

    # endpoints
    ENDPOINTS = [
        "cetb",
        "prog",
    ]


conf = Config()

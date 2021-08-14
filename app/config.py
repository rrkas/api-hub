import secrets


class Config:
    # api name
    NAME = 'api-hub'

    SECRET_KEY = secrets.token_hex(8)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # home
    CREATOR = "Rohnak Agarwal"
    VERSION = "1.0.0"

    # endpoints
    ENDPOINTS = [
        "cetb",
    ]




conf = Config()

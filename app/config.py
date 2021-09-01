import os
import secrets

from flask import current_app, request

static_path = os.path.normpath(current_app.root_path)
static_path = os.sep.join(os.path.split(static_path)[:-1])


class Config:
    # api name
    NAME = "{ api-hub }"

    SECRET_KEY = secrets.token_hex(8)
    OUTPUT_DIR = os.path.join(static_path, "output")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # links
    POSTMAN_COLLECTION_URL = (
        "https://www.getpostman.com/collections/87ab6adecba171c3525c"
    )
    GITHUB_REPO_URL = "https://github.com/rrkas/api-hub"

    # home
    CREATOR = "Rohnak Agarwal"
    PROJECT_START_DATE = "14 August, 2021"
    VERSION = "1.0.0"

    app_base_url = None
    json_indent = 4


conf = Config()

with current_app.test_request_context("/"):
    conf.app_base_url = request.host_url

if not os.path.exists(conf.OUTPUT_DIR):
    os.makedirs(conf.OUTPUT_DIR)

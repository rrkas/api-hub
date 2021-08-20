from flask import request


class Documentation:
    def __init__(
        self,
        name: str,
        endpoint: str,
        methods: list = ["GET"],
        args: dict = {},
        description: str = "",
        body: dict = {},
        example_request: dict = {},
    ):
        self.name = name
        self.endpoint = endpoint
        self.methods = methods
        self.description = description
        self.args = args
        self.body = body
        self.example_request = example_request


current_dns = request.endpoint

from hvac import Client


class TokenClient(Client):
    def __init__(self, token, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token

    @staticmethod
    def parse_token(path):
        with open(path) as stream:
            return json.loads(stream.read())["token"]

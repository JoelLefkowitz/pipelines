#!/usr/bin/env python
import json
import os
from secrets import token_bytes

from simple_pipes import pipe_call

from hvac import Client

if __name__ == "__main__":
    with open("/tokens/postgres.json") as stream:
        client = Client("https://vault:8200")
        client.token = json.loads(stream.read())["token"]

    password = str(token_bytes(16))

    client.write(f"postgres", password)
    os.environ["POSTGRES_PASSWORD"] = password
    pipe_call(["postgres"])

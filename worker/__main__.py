#!/usr/bin/env python

import json
from secrets import token_bytes

from simple_pipes import pipe_call

import hvac
from utils import get_unique_name

if __name__ == "__main__":
    with open("/tokens/worker.json") as stream:
        client = hvac.Client("https://vault:8200")
        client.token = json.loads(stream.read())["token"]

    name = get_unique_name(client.list("workers").keys())
    password = str(token_bytes(16))

    client.write(f"workers/{name}", password)

    pipe_call(
        [
            "buildbot-worker",
            "create-worker",
            ".",
            "master:9989",
            name,
            password,
        ]
    )

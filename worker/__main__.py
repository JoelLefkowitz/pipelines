#!/usr/bin/env python

from secrets import token_bytes

from simple_pipes import pipe_call

from src.token import TokenClient
from utils import get_unique_name

if __name__ == "__main__":
    token = TokenClient.parse_token("/tokens/worker.json")
    client = TokenClient("https://vault:8200", token)

    worker_names = client.list("workers").keys()
    name = get_unique_name(worker_names)
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

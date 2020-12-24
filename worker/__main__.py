#!/usr/bin/env python

from secrets import token_bytes

from buildbot_abstract import TokenClient, get_unique_name
from simple_pipes import pipe_call

if __name__ == "__main__":
    client = TokenClient.try_token_path("/tokens/worker/token.json")
    workers = client.list("workers")
    name = get_unique_name(workers.keys() if workers else [])
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

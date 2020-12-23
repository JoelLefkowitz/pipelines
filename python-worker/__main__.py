#!/usr/bin/env python

from secrets import token_bytes

from simple_pipes import pipe_call

from clients import TokenClient, get_unique_name

if __name__ == "__main__":
    client = TokenClient.try_token_path("/tokens/postgres/token.json")
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

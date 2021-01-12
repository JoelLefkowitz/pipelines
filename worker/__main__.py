#!/usr/bin/env python
from secrets import token_bytes

from buildbot_abstract import TokenClient, get_unique_name
from simple_pipes import pipe_call


def client_work():
    print("Creating a vault client")
    client = TokenClient.try_token_path(
        url="http://vault:8200", path="/tokens/worker/token.json"
    )

    print("Retrieving registered workers")
    workers = client.list("workers")

    name = get_unique_name(workers.keys() if workers else [])
    password = str(token_bytes(16))

    print("Registering a unique worker")
    client.write(f"workers/{name}", password)
    return name, password


if __name__ == "__main__":
    cmd = ["buildbot-worker", "create-worker", ".", "master:9989"]
    name, password = client_work()

    print("Running buildbot-worker create-worker")
    pipe_call([*cmd, name, password])

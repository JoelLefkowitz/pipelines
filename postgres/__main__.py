#!/usr/bin/env python
import os
from secrets import token_bytes

from buildbot_abstract import TokenClient

import pipe_call


def client_work():
    print("Creating a vault client")
    client = TokenClient.try_token_path(
        url="http://vault:8200/", path="/tokens/postgres/token.json"
    )

    password = str(token_bytes(16))
    print("Registering a postgres password")

    client.secrets.kv.v1.create_or_update_secret(
        path="postgres",
        secret=password,
    )
    return password


if __name__ == "__main__":
    password = client_work()

    print("Setting the POSTGRES_PASSWORD environment")
    os.environ["POSTGRES_PASSWORD"] = password

    print("Running docker-entrypoint.sh")
    pipe_call(["bash", "/docker-entrypoint.sh"])

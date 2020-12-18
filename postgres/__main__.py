#!/usr/bin/env python
import os
from secrets import token_bytes

from simple_pipes import pipe_call

from clients import TokenClient

if __name__ == "__main__":
    client = TokenClient.try_token_path("/tokens/postgres/token.json")
    password = str(token_bytes(16))
    client.write("postgres", password)
    os.environ["POSTGRES_PASSWORD"] = password
    pipe_call(["postgres"])

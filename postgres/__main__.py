#!/usr/bin/env python
import os
from secrets import token_bytes

from simple_pipes import pipe_call

from clients import TokenClient

if __name__ == "__main__":
    token = TokenClient.parse_token("/tokens/postgres/token.json")
    client = TokenClient(token)
    password = str(token_bytes(16))
    client.write("postgres", password)
    os.environ["POSTGRES_PASSWORD"] = password
    pipe_call(["postgres"])

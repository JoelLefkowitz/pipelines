#!/usr/bin/env python
from secrets import token_bytes

from safe_environ import from_env
from simple_pipes import pipe_call

from registration import get_unique_name, list_worker_entries, post_worker_data

if __name__ == "__main__":
    vault_host = "0.0.0.0"
    buildmaster = "master"

    vault_port = 8200
    buildmaster_port = 9989

    token = from_env("VAULT_TOKEN")
    registered_workers = list_worker_entries(vault_host, vault_port, token)

    name = get_unique_name(registered_workers.keys())
    password = str(token_bytes(16))

    post_worker_data(vault_host, vault_port, name, password, token)
    pipe_call(
        [
            "buildbot-worker",
            "create-worker",
            ".",
            f"{buildmaster}:{buildmaster_port}",
            name,
            password,
        ]
    )

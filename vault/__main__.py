#!/usr/bin/env python
import multiprocessing
from time import sleep

from simple_pipes import pipe_call
from vault_wrapper import VaultClient, VaultPolicy


def client_work():
    sleep(5)

    client = VaultClient(unseal=True)
    client.enable_kv_engines(["workers", "postgres"])

    client.create_policies(
        [
            VaultPolicy("master", {"workers": ["list", "read"], "postgres": ["read"]}),
            VaultPolicy("worker", {"workers": ["list", "create"]}),
            VaultPolicy("postgres", {"postgres": ["create"]}),
        ]
    )

    client.write_tokens(["master", "worker", "postgres"])


if __name__ == "__main__":
    multiprocessing.Process(target=client_work).start()
    pipe_call(["vault", "server", "-config=vault/config.hcl"])

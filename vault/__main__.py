#!/usr/bin/env python
import multiprocessing

from simple_pipes import pipe_call
from vault_wrapper import VaultClient, VaultPolicy


def client_work():
    print("Creating a vault client")
    client = VaultClient.try_connect_client(
        url="http://127.0.0.1:8200", unseal=True
    )

    print("Enabling workers and postgres kv engines")
    client.enable_kv_engines(["workers", "postgres"])

    print("Creating master, worker and postgres policies")
    client.create_policies(
        [
            VaultPolicy(
                "master",
                {"workers": ["list", "read"], "postgres": ["read"]},
            ),
            VaultPolicy("worker", {"workers": ["list", "create"]}),
            VaultPolicy("postgres", {"postgres": ["create"]}),
        ]
    )

    print("Writting master, worker and postgres api tokens")
    client.write_tokens(["master", "worker", "postgres"])


if __name__ == "__main__":
    print("Forking a vault client process")
    multiprocessing.Process(target=client_work).start()

    print("Starting vault server")
    pipe_call(["vault", "server", "-config=vault/config.hcl"])

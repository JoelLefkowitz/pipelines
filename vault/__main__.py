#!/usr/bin/env python

from policy import VaultPolicy
from client import VaultClient

if __name__ == "__main__":
    client = VaultClient(unseal=True)
    client.enable_kv_engines(["workers", "postgres"])

    client.create_policies(
        [
            VaultPolicy("master", read=["workers", "postgres"]),
            VaultPolicy("worker", write=["workers"]),
            VaultPolicy("postgres", write=["postgres"]),
        ]
    )

    client.write_tokens(["master", "worker", "postgres"])

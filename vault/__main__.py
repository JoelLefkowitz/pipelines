#!/usr/bin/env python

from client import VaultClient
from policy import VaultPolicy

if __name__ == "__main__":
    client = VaultClient(unseal=True)
    client.enable_kv_engines(["workers", "postgres"])

    client.create_policies(
        [
            VaultPolicy("master", {"workers": ["list", "read"], "postgres": ["read"]}),
            VaultPolicy("worker", {"workers": ["list", "write"]}),
            VaultPolicy("postgres", {"postgres": ["write"]}),
        ]
    )

    client.write_tokens(["master", "worker", "postgres"])

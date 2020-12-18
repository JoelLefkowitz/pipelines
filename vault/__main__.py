#!/usr/bin/env python

import subprocess

from clients import VaultClient, VaultPolicy

if __name__ == "__main__":
    subprocess.Popen(
        ["vault", "server", f"-config=vault/config.hcl"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

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

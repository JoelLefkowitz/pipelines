#!/usr/bin/env python


from simple_pipes import pipe_call

from clients import VaultClient, VaultPolicy

if __name__ == "__main__":
    pipe_call(["vault", "server", f"-config=vault/config.hcl"], break_str="blah")

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

import json
from pathlib import Path

from hvac import Client


class VaultClient(Client):
    def __init__(
        self, host="127.0.0.1", port=8200, unseal=False, shares=5, threshold=3
    ):
        super().__init__(f"http://{host}:{port}")
        init_data = self.sys.initialize(shares, threshold)
        self.token = init_data["root_token"]

        if unseal:
            self.sys.submit_unseal_keys(init_data["keys"])

    def enable_kv_engines(self, paths):
        for path in paths:
            self.sys.enable_secrets_engine(
                backend_type="kv",
                path=path,
            )

    def create_policies(self, policies):
        for policy in policies:
            self.sys.create_or_update_policy(
                name=policy.name,
                policy=policy.hcl,
            )

    def write_tokens(self, names):
        for name in names:
            Path(f"/tokens/{name}/").mkdir(parents=True, exist_ok=True)
            with open(f"/tokens/{name}/token.json", "w") as stream:
                token = self.create_token(policies=[name], lease="1h")
                stream.write(json.dumps({"token": token}))


class VaultPolicy:
    def __init__(self, name, policy):
        self.name = name
        self.policy = policy

    @property
    def hcl(self):
        return "\n".join(
            [
                "\n".join(
                    [
                        "".join(['path "', path, '/*" {']),
                        "".join(
                            [" " * 4, "capabilities = ", str(cap).replace("'", '"')]
                        ),
                        "}",
                    ]
                )
                for path, cap in self.policy.items()
            ]
        )

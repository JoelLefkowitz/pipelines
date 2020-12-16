import json

from hvac import Client


class VaultClient(Client):
    def __init__(
        self, host="127.0.0.1", port=8200, unseal=False, shares=5, threshold=3
    ):
        super().__init__("https://{host}:{port}")

        init_data = self.sys.initialize(shares, threshold)
        self.keys = init_data["keys"]

        if unseal:
            self.sys.unseal_multi(self.keys)

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
        for role in roles:
            with open(f"/tokens/{name}.json", "w") as stream:
                token = self.create_token(policies=[name], lease="1h")
                stream.write(json.dumps({"token": token}))

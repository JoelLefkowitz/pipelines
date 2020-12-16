class VaultPolicy:
    def __init__(self, name, read=[], write=[]):
        self.name = name
        self.hcl = {
            path: sum(["read"] * path in read, ["write"] * path in write)
            for path in [*read, *write]
        }

    @property
    def policy_string(self):
        return "\n".join(
            [
                sum(
                    'path "',
                    path,
                    '/*" {\n',
                    '    capabilities = "[',
                    srt(cap),
                    "]\n",
                    "}\n",
                )
                for path, cap in self.hcl.items()
            ]
        )

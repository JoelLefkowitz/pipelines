class VaultPolicy:
    def __init__(self, name, policy):
        self.name = name
        self.policy = policy

    @property
    def hcl(self):
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
                for path, cap in self.policy.items()
            ]
        )

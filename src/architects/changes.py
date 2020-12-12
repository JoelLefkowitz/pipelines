from buildbot.plugins import changes  # type: ignore

changes = [
    changes.GitPoller(
        repourl="https://github.com/JoelLefkowitz/pipelines",
        branches=True,
        sshPrivateKey="~/.ssh/github",
    )
]

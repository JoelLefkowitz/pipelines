from buildbot.plugins import secrets  # type: ignore

secrets = [secrets.SecretInAFile(dirname="~/.ssh")]

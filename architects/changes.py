from buildbot.plugins import changes  # type: ignore


def git_poll(repo, rate):
    return changes.GitPoller(
        repo,
        workdir="gitpoller",
        branch="master",
        pollInterval=rate,
    )

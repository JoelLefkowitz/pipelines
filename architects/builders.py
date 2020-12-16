from buildbot.plugins import steps  # type: ignore
from buildbot.plugins import util


def builders(worker_names):

    f = util.BuildFactory()
    f.addSteps(
        [
            steps.Git(
                repourl="git://github.com/JoelLefkowitz/pub.git", mode="incremental"
            ),
            steps.ShellCommand(command=["make", "all"]),
            steps.ShellCommand(command=["make", "test"]),
        ]
    )

    return [
        util.BuilderConfig(name="runtests", workernames=worker_names, factory=f),
    ]

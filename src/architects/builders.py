from buildbot.plugins import steps  # type: ignore
from buildbot.plugins import util


def builders(workers):
    return [
        util.BuilderConfig(
            name="runtests",
            workernames=[i.name for i in workers],
            factory=util.BuildFactory(
                [steps.ShellCommand(name="pytest", command=["pytest"])]
            ),
        ),
    ]

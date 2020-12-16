from buildbot.plugins import schedulers  # type: ignore

schedulers = [
    schedulers.SingleBranchScheduler(
        name="tester", builderNames=["runtests"], branch="master"
    )
]

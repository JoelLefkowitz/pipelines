from buildbot.plugins import worker  # type: ignore
from randutils import random_string  # type: ignore


def pool(n):
    return [worker.Worker(f"Worker{i}", random_string(20)) for i in range(n)]

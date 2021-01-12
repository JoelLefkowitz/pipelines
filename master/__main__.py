#!/usr/bin/env python
from simple_pipes import pipe_call

if __name__ == "__main__":
    print("Running buildbot start")
    pipe_call(["buildbot", "start"])

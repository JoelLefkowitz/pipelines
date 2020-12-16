import os


def set_worker_env(name, password):
    os.environ["WORKERNAME"] = name
    os.environ["WORKERPASS"] = password

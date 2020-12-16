import json

from buildbot.plugins import worker

from hvac import Client


class MasterClient(Client):
    def __init__(self):
        with open("/tokens/master.json") as stream:
            super().__init__("https://vault:8200")
            self.token = json.loads(stream.read())["token"]

    @property
    def postgres(self):
        return self.read("postgres")

    @property
    def worker_names(self):
        return self.list("workers")

    @property
    def workers(self):
        return [
            worker.Worker(worker_name, client.get(f"/workers/{worker_name}"))
            for worker_name in client.worker_names
        ]

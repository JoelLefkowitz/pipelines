import hvac


def set_postres_password(name, password):
    client = hvac.Client()
    client.secrets.kv.v1.list_secrets(path="postgres")


def get_postres_kv(name):
    client = hvac.Client()
    read_secret_result = client.secrets.kv.v1.read_secret(
        path="postgres",
        mount_point="pipelines",
    )


def set_worker_kv(name, password):
    client = hvac.Client()
    client.secrets.kv.v1.list_secrets(path="worker")


def get_worker_kv(name):
    client = hvac.Client()
    client.secrets.kv.v1.list_secrets(path="workers")


def list_worker_kv():
    client = hvac.Client()
    client.secrets.kv.v1.list_secrets(path="workers")

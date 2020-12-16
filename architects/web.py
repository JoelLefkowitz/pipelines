def buildbot_url(host, port):
    return f"http://{host}:{port}/"


def www(port):
    return {
        "port": port,
        "plugins": {"waterfall_view": {}, "console_view": {}, "grid_view": {}},
    }

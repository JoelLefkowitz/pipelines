import urllib.parse

sqlite = {"db_url": "sqlite:///state.sqlite"}


def postgres(host, db_name, user, password):
    url = f"{user}:{urllib.parse.quote_plus(password)}@{host}/{db_name}"
    return {"db_url": f"postgresql+psycopg2://{url}"}

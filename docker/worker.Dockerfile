FROM python:3.8-buster

WORKDIR /pipelines
COPY setup.py setup.py

RUN pip install .[worker]
COPY registration registration

COPY worker .
ENTRYPOINT ["python", "worker"]

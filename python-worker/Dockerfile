FROM python:3.8-buster

WORKDIR /pipelines
COPY setup.py setup.py
RUN pip install .

COPY worker worker
ENTRYPOINT ["python", "worker"]

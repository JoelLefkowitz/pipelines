FROM python:3.8-buster
WORKDIR /pipelines

COPY setup.py setup.py
RUN pip install .[master]

RUN buildbot create-master
RUN rm master.cfg.sample

COPY master master
ENTRYPOINT ["python", "master"]
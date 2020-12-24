FROM python:3.8-buster
WORKDIR /pipelines

COPY setup.py setup.py
RUN pip install .

WORKDIR /pipelines/master
RUN buildbot create-master
RUN rm master.cfg.sample

COPY master /pipelines/master
ENTRYPOINT ["python", "/pipelines/master"]
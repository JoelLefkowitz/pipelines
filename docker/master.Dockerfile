FROM python:3.8-buster
WORKDIR /pipelines

COPY setup.py setup.py
RUN pip install .

RUN buildbot create-master
RUN rm master.cfg.sample

COPY architects architects
COPY registration registration

COPY master .
ENTRYPOINT ["python", "master"]
FROM python:3.8-buster
WORKDIR /pipelines

COPY setup.py setup.py
RUN pip install .

RUN buildbot create-master -c master/master.cfg
RUN rm master.cfg.sample

COPY master master
ENTRYPOINT ["python", "master"]
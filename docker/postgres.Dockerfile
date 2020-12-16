FROM postgres:13
WORKDIR /pipelines

RUN apt-get update 
RUN apt-get install -y python3.6
RUN apt-get install -y python3-pip
RUN pip install setuptools

COPY setup.py setup.py
RUN pip install .[postgres]
COPY postgres .

ENTRYPOINT ["python", "postgres"]
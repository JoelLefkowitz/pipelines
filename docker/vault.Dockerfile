FROM vault:1.6.0
WORKDIR /pipelines

RUN apt-get update 
RUN apt-get install -y python3.6
RUN apt-get install -y python3-pip
RUN pip install setuptools

COPY setup.py setup.py
RUN pip install .[vault]
COPY vault .

ENTRYPOINT ["python", "vault"]

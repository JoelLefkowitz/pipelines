FROM postgres:13
WORKDIR /pipelines

RUN apt update 
RUN apt install -y python3
RUN apt install -y python3-pip

RUN ln -sf python3 /usr/bin/python 
RUN pip3 install --no-cache --upgrade pip setuptools

COPY setup.py setup.py
RUN pip install .

COPY postgres postgres
COPY clients postgres/clients
ENTRYPOINT ["python", "postgres"]
FROM vault:1.6.0
WORKDIR /pipelines

RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools

RUN ln -sf python3 /usr/bin/python
RUN pip3 install --no-cache --upgrade pip setuptools

COPY setup.py setup.py
RUN pip install .

COPY vault vault
ENTRYPOINT ["python", "/pipelines/vault"]

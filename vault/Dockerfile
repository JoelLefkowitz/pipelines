FROM vault:1.6.0
WORKDIR /pipelines

RUN apk add --update --no-cache python3

RUN ln -sf python3 /usr/bin/python
RUN python -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

COPY setup.py setup.py
RUN pip install .[vault]

COPY vault vault
ENTRYPOINT ["python", "vault"]

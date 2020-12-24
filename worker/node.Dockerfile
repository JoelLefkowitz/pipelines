FROM node:15.5-buster

RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip

RUN ln -sf python3 /usr/bin/python 
RUN pip3 install --no-cache --upgrade pip setuptools

WORKDIR /pipelines
ENV PATH /smoothycode/node_modules/.bin:$PATH

COPY package.json .
RUN npm i

COPY setup.py .
RUN pip install .

COPY worker worker
ENTRYPOINT ["python", "/pipelines/worker"]

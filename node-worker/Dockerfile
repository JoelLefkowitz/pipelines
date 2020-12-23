FROM node:14.9 AS build

# Setup environment
WORKDIR /build
ENV PATH /build/node_modules/.bin:$PATH

# Build and cache dependencies
COPY package.json .
RUN npm i

# Copy source
COPY Gruntfile.js routines.yml ./
COPY node-worker node-worker

# Build target
RUN grunt buildNodeWorker
ENTRYPOINT [ "node", "/build/node-worker/dist/main.js" ]
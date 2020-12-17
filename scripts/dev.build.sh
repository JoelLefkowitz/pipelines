#!/bin/sh
set -e

cd $(dirname $BASH_SOURCE)
cd ../

version=0.1.0_dev
dockerfiles="master worker vault postgres"

for target in $dockerfiles
do
docker build . \
    -f $target/Dockerfile \
    -t joellefkowitz/pipeline_$target:$version
done

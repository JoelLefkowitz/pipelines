#!/bin/sh
set -e

cd $(dirname $BASH_SOURCE)
cd ../../

for target in "master worker vault postgres"
do
docker build . \
    -f docker/$target.Dockerfile \
    -t joellefkowitz/pipeline_$target:0.1.0_dev
done

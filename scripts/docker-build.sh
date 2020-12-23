#!/bin/sh
set -e

cd $(dirname $BASH_SOURCE)
cd ..

trim() {
    echo ${1:0:${#1}-$2}
}

version="${1:-0.1.0_dev}"

for dir in */; do
    dockerfile=${dir}Dockerfile

    if test -f $dockerfile; then
        service=$(trim ${dir//-/_} 1)
    
        docker build . \
            -f $dockerfile \
            -t joellefkowitz/pipelines_$service:$version
    fi
done

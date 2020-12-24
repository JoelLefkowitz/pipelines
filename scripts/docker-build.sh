#!/bin/sh
set -e

cd $(dirname $BASH_SOURCE)
cd ..

trim() {
    echo ${1:0:${#1}-$2}
}

for dir in */; do
    for dockerfile in ${dir}*Dockerfile; do
        if [ -f "$dockerfile" ]; then 
                
            root="joellefkowitz/pipelines_"
            service=$(trim ${dir//-/_} 1)
            
            path=$(trim ${dockerfile//./_} 10)
            prefix=${path##*/}
            
            version="${1:-0.1.0_dev}"

            docker build . \
                -f $dockerfile  \
                -t $root$prefix$service:$version
        fi
    done
done

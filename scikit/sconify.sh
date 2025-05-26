#!/bin/bash

# Declare the app entrypoint
ENTRYPOINT="python3 /app/app.py"

# Declare image related variables
IMG_NAME=scikit
IMG_FROM=aimendjari/scikit:1.0.0
IMG_TO=aimendjari/${IMG_NAME}:1.0.0-debug

# Run the sconifier to build the TEE image based on the non-TEE image
docker run -it \
            -v /var/run/docker.sock:/var/run/docker.sock \
            registry.scontain.com/scone-production/iexec-sconify-image:5.9.0-v15 \
	    sconify_iexec \
            --name=${IMG_NAME} \
	    --from=${IMG_FROM} \
            --to=${IMG_TO} \
	    --base=python:3.9-bullseye \
            --binary-fs \
            --fs-dir=/app \
            --host-path=/etc/hosts \
            --host-path=/etc/resolv.conf \
            --binary=/usr/local/bin/python3 \
            --disable-binary-symlink-detection \
	    --heap=4G \
            --dlopen=1 \
            --no-color \
            --verbose \
            --command=${ENTRYPOINT} \
            && echo -e "\n------------------\n" \
            && echo "successfully built TEE docker image => ${IMG_TO}" \
            && echo "application mrenclave.fingerprint is $(docker run --rm -e SCONE_HASH=1 ${IMG_TO})"


#!/usr/bin/bash

# build the image
docker build --tag zipline-challenge .

# export it to a tarball
docker save zipline-challenge > zipline-challenge.docker.tar

#!/bin/bash
set -e
set -u

source ./docker_config.sh

# for example, if your deployment key is ` ~/.ssh/id_rsa`
SSH_PRIVATE_KEY=''  # $(cat ~/.ssh/id_rsa)

docker build -t "${docker_image_tag:?}" . --build-arg="SSH_PRIVATE_KEY=$SSH_PRIVATE_KEY" --no-cache

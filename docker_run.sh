#!/bin/bash
set -e
set -u

source ./docker_config.sh

# to remove old container and run
(docker rm "${docker_image_tag:?}" &> /dev/null && echo "removed old container ${docker_image_tag:?}") || true
# assign container a name by --name, given a docker image
docker run \
--name "${docker_image_tag:?}" \
-it \
"${docker_image_tag:?}"

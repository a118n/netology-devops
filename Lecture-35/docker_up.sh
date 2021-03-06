#!/usr/bin/env bash

set -euo pipefail

echo "Starting containers..."
docker run -dit --name centos-es centos:7
docker exec -it centos-es bash -c 'yum install -y sudo'
docker run -dit --name centos-ls centos:7
docker exec -it centos-ls bash -c 'yum install -y sudo'
echo "Containers started."

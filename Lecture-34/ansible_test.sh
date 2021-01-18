#!/usr/bin/env bash

set -euo pipefail

docker run -dit --name centos7 centos:7
docker run -dit --name ubuntu ubuntu
docker exec -it ubuntu bash -c 'apt update && apt install -y python3'
docker run -dit --name fedora pycontribs/fedora

cd ./playbook
ansible-playbook --ask-vault-pass -i inventory/prod.yml site.yml

docker container stop {centos7,ubuntu,fedora}

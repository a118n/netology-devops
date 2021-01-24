#!/usr/bin/env bash

set -euo pipefail

ansible-galaxy install -r requirements.yml -p roles
docker run -dit --name centos8 centos:8
docker exec -it centos8 bash -c 'yum install -y sudo'
ansible-playbook -i inventory/inventory.yml install-elk.yml

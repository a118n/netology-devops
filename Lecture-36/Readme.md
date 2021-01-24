# ES & Kibana playbook with roles

## Description
This is a sample playbook to install ElasticSearch & Kibana on a docker container.

Playbook uses the following roles:
* [java](https://github.com/netology-code/mnt-homeworks-ansible)
* [elastic-role](https://github.com/a118n/elastic-role)
* [kibana-role](https://github.com/a118n/kibana-role)

The included `install.sh` script will do everything automatically:
* Download & install the aforementioned roles to **roles** folder in current directory
* Run the container
* Run the playbook

## Requirements
* Ansible >= 2.10
* Docker >= 20.10

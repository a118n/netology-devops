# ELK stack installation playbook

## This playbook does the following:

1. Installs Java

   You can specify Java version in `group_vars/all/vars.yml`.

   You have to manually [download](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) Java tar.gz archive and place it in the **files** directory. Be sure to check the `java_oracle_jdk_package` variable to match the archive filename.

   Java is installed in the `/opt/jdk/$java_jdk_version/` directory.

2. Installs Elasticsearch

   You can specify Elasticsearch version in `group_vars/elasticsearch/vars.yml`.

   Elasticsearch is installed into `/opt/elastic/$elastic_version/` directory.

3. Installs Kibana

   You can specify Kibana version in `group_vars/elasticsearch/vars.yml`.

   Kibana is installed `/opt/kibana/$kibana_version/` directory.

4. Installs Logstash

   **Logstash is installed on a separate host**.

   You can specify Logstash version in `group_vars/logstash/vars.yml`.

   Logstash is installed `/opt/logstash/$logstash_version/` directory.

## Notes:
By default this playbook uses single docker container with the name **centos-es** for Elasticsearch & Kibana, and another separate container with the name **centos-ls** for Logstash. You must have the containers running prior to executing this playbook.

To run the containers, use the following commands:
```
docker run -dit --name centos-es centos:7
docker exec -it centos-es bash -c 'yum install -y sudo'
docker run -dit --name centos-ls centos:7
docker exec -it centos-ls bash -c 'yum install -y sudo'
```
Or just use `docker_up.sh` script.

Of course, you can change it to anything else in the `inventory/prod.yml` file.

## Available tags:
* java
* elastic
* kibana
* logstash
* skip_ansible_lint

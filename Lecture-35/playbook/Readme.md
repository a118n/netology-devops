## This playbook does the following:

1. Installs Java

   You can specify Java version in `group_vars\all\vars.yml`.

   You have to manually [download](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) Java tar.gz archive and place it in the **files** directory. Be sure to check the `java_oracle_jdk_package` variable to match the archive filename.

   Java installs in the `/opt/jdk/$java_jdk_version/` directory.

2. Installs Elasticsearch

   You can specify Elasticsearch version in `group_vars/elasticsearch/vars.yml`.

   Elasticsearch installs into `/opt/elastic/$elastic_version/` directory.

3. Installs Kibana

   You can specify Kibana version in `group_vars/elasticsearch/vars.yml`.

   Kibana installs into `/opt/kibana/$kibana_version/` directory.

## Notes
By default this playbook uses single docker container with the name **centos-elk**. You must have the container running prior to executing this playbook.

To run the container, use the following commands:
```
docker run -dit --name centos-elk centos:7
docker exec -it centos-elk bash -c 'yum install -y sudo'
```
Of course, you can change it to anything else in the `inventory/prod.yml` file.

## Available tags:
* java
* elastic
* kibana
* skip_ansible_lint

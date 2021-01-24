Kibana Role for Ansible
=========

Download and install Kibana from official website

Requirements
------------

Java

Role Variables
--------------
```yaml
kibana_version: "7.10.1"
kibana_home: "/opt/kibana/{{ kibana_version }}"
```

Example Playbook
----------------

```yaml
- hosts: all
  roles:
      - kibana
```

License
-------

BSD

Author Information
------------------

[Daniel Allen](https://github.com/a118n)

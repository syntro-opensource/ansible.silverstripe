# Ansible Role: silverstripe

[![Ansible Role](https://img.shields.io/ansible/role/51272?color=darkred&logo=ansible)](https://galaxy.ansible.com/syntro_gmbh/silverstripe)
![Molecule test](https://github.com/syntro-opensource/ansible.silverstripe/workflows/Molecule%20test/badge.svg)
[![Ansible Quality Score](https://img.shields.io/ansible/quality/51272?logo=ansible)](https://galaxy.ansible.com/syntro_gmbh/silverstripe)
[![Ansible Role](https://img.shields.io/ansible/role/d/51272?color=success&logo=ansible)](https://galaxy.ansible.com/syntro_gmbh/silverstripe)

## Description

[Silverstripe](https://www.silverstripe.org) is a versatile open source framework
for websites. This role deploys a Silverstripe installation of your choice to a
LAMP server.

Key features of this role include:
* **Minimal reqiurements for deployment** *-> deploy anywhere*
* **Release retention** *-> roll back quickly in the case of an error*
* **Downtimeless deployment** *-> deploy without interrupting usage*
* **CI ready** *-> specify tags or keep branches up to date*
* **Backup friendly** *-> run backup scripts before flushing and building*


### Downtimeless Deployment

By default, this role deploys any version downtimeless. This means, that the
build and flush processes will happen before the actual codebase is linked to
be used by `html/index.php`. This brings some advantages as no user is locked
out from using the site which makes deployments possible during uptime-crucial
times. Silverstripe is in most cases capable of being deployed this way, as the
database structure is mostly backwards compatible. The only times at the time of
writing this readme where this could lead to problems are:

* Removing DataObjects
  * Silvertripe dosen't remove the Table, but prefixes it with `deprecated_`
* Changing Enum values

These scenarios are very specific and should in theory not happen as it would
be a sign of bad planning on the developer side.

However, this may also lead to problems database backups, as additional care
has to be taken in order to get consistent backups! This responsibility is
to be taken by the user of this role.


## Installation
```
ansible-galaxy install syntro_gmbh.silverstripe
```

## Requirements

* Composer
* Git

## Dependencies

None, but make sure to have composer and git installed on the host you are deploying to.

## Usage
Apart from a few required variables, this role can simply be used for any
silverstripe project. Have a look on the [defaults](defaults/main.yml) file
to get an idea of what you can customize.

### The webroot and the files generated
This role uses the following directory structure to serve your application:

```
{{ WorkingDir }}/
├── {{ current }}
│   ├── .htaccess
│   ├── index.php
│   ├── assets --> ../shared/assets
│   └── _resources --> ../releases/<current sha>/_resources
├── releases/
│   ├── <current sha>/
│   │   ├── .git
│   │   └── ...
│   └── <other sha>/
│       ├── .git
│       └── ...
├── shared/
│   └── assets/
└── logs/
```

your webroot should point to the `{{ WorkingDir }}/{{ current }}/` directory.
You can configure these directories using [`silverstripe_working_dir`](defaults/main.yml)
and [`silverstripe_current_dir_name`](defaults/main.yml), respectively.


### Building and updating the database and running backups
In order to get Silverstripe working with a new install, one has to build or
update the database. By default, this role executes the standard build
task combined with the `flush=1` parameter before updating any files in the
webroot.

You can add more commands, but **don't forget to re-add** the build command
using the [`silverstripe_provisioning_cmds`](defaults/main.yml). This is also
the place to add any backup commands you might need. (You might use our
[restic role](https://github.com/arillso/ansible.restic) to install a backup
utility and create the scripts automatically.) by adding these scripts before
the build step, you get the most recent version of your installation in case
you need to roll back.

### Downtimeless deployment
This role deploys silverstripe version downtimeless. This means, that the
build and flush processes will happen before the actual codebase is linked to
be used by `index.php`. This brings some advantages as no user is locked
out from using the site which makes deployments possible at any time.
Silverstripe is in most cases capable of being deployed this way, as the
database structure is mostly backwards compatible. The only times at the time of
writing this readme where this could lead to problems are:

* Removing DataObjects
  * Silvertripe dosen't remove the Table, but prefixes it with `deprecated_`
* Changing Enum values

These scenarios are very specific and should in theory not happen as it would
be a sign of bad planning on the developer side. Nevertheless, you should always
create a backup of the database before updating.


## Role Variables
Check the [defaults](defaults/main.yml) file to get an idea of what you can
control.

## Minimal example playbook

```yaml
- hosts: all
  vars:
    silverstripe_project_repository: https://github.com/silverstripe/demo.silverstripe.org
    silverstripe_project_version: master
    silverstripe_ss_database_name: silverstripe
    silverstripe_ss_database_username: root
    silverstripe_ss_database_password: root
  roles:
    - silverstripe
```


## Author

- Matthias Leutenegger

## License

MIT

## Copyright

(c) 2020, Syntro GmbH

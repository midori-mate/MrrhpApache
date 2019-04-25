Mrrhp Apache
===

## Installation

```
$ git clone https://gitlab.com/midori-mate/mrrhpapache.git
```


## Open on virtual environment THROUGH Apache

Install them.

- [Vagrant](https://www.vagrantup.com/)
- [Virtualbox](https://www.virtualbox.org/)

**Windows user has to open Powershell as Administrator!** Or you cannot create symbolic links and setup will fail.

```
$ vagrant up
$ vagrant ssh
```

In the virtual env.

```
$ source /vagrant/env3.6/bin/activate
$ python /vagrant/manage.py createsuperuser --settings=config.settings.production
```

Access [localhost:1991/](http://localhost:1991/) then.  
Access [localhost:1991/admin/](http://localhost:1991/admin/) as well.

Close the env.

```
$ exit
$ vagrant halt
```


## After tweating static files

You have to check that there are no 404 files with `runserver` and through Apache as well.

Before checking through Apache you have to use these commands.

```
$ source /vagrant/env3.6/bin/activate
$ python /vagrant/manage.py collectstatic -c --noinput
$ sudo apachectl restart
```

And then you can commit!


## After /fixtures/initial_db_data.json modified

You have to run the command below to register data to your own db.

On local env.

```
$ python manage.py loaddata initial_db_data.json
```

On virtual env.

```
$ source /vagrant/env3.6/bin/activate
(env3.6) [~]$ python /vagrant/manage.py loaddata /vagrant/fixtures/initial_db_data.json --settings=config.settings.production
```

## Useful commands

```
$ sudo apachectl restart
$ sudo systemctl restart mysqld
$ python /vagrant/manage.py makemigrations --settings=config.settings.production
$ python /vagrant/manage.py migrate --settings=config.settings.production
$ python /vagrant/manage.py dumpdata app > /vagrant/fixtures/initial_db_data.json --settings=config.settings.production
$ python /vagrant/manage.py loaddata /vagrant/fixtures/initial_db_data.json --settings=config.settings.production
$ sudo tail -f /var/log/httpd/error_log
$ sudo tail -f /var/log/httpd/access_log
$ systemctl enable httpd.service
$ systemctl disable httpd.service
$ systemctl list-unit-files -t service | grep httpd
$ systemctl status firewalld.service
```


## Open on local

Access [localhost:8000/](http://localhost:8000/) then.  
Access [localhost:8000/admin/](http://localhost:8000/admin/) as well.


## Open DB with MySQLworkbench

```
$ vagrant ssh
```

```
$ sudo mysql -u root -p
password
MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO root@'192.168.33.1' IDENTIFIED BY 'password';
```

Access through Workbench.

| Hostname      | Username | Password | Default Schema |
| ------------- | -------- | -------- | -------------- |
| 192.168.33.12 | root     | password | app            |

If you fail to access, check the error message to remake access user again.

```
MariaDB [(none)]> DROP USER 'root'@'192.168.33.1';
```

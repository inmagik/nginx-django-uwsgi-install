# nginx-django-wsgi-install
Notes on installation of web stack. will become the base for some ansible playbooks

This installation is meant to be used in an Ubuntu machine

# Server environment

## updating repos
```
sudo apt-get update
```

## virtualenv
```
sudo apt-get install python-virtualenv
sudo apt-get install python-pip
```

## python packages build dependencies
```
sudo apt-get install python-dev
```


### installing 
```
sudo apt-get install python-virtualenv 
```

## nginx

### installing
```
sudo apt-get install nginx
```
### basic configuration

## supervisord
### installing
```
apt-get install supervisor
```

# uwsgi
## installing
```
pip install uwsgi
```

# Server app deployment
## clone git repository
## create virtual environment
Environment will be located inside the server app repo

## config templates variables
Templates are included for the various config files. 
They use Jinja template syntax, the following variables are required:


* `SERVER_APP_NAME`
* `SERVER_APP_SOCKET_PATH`
* `SERVER_APP_SOCKET_PORT`
* `SERVER_APP_DOMAIN`
* `SERVER_APP_MEDIA_FOLDER`
* `SERVER_APP_STATIC_FOLDER`
* `SERVER_APP_WSGI_PARAMS_PATH`



## uwsgi config
A sample uwsgi config for a django project is included in `uwsgi.ini.template` 


## nginx config
A sample nginx config for a django project is included in `nginx.conf.template`

## supervisor config
Supervisor will be configured to:
* monitor nginx
* monitor uwsgi process

## bonus: postgresql
### installing
### enabling access from local machine



# template scripts

# nginx-django-uwsgi-install
Notes on installation of web stack. will become the base for some ansible playbooks

This installation is meant to be used in an Ubuntu machine

# Server environment

## updating repos and installing git
```
sudo apt-get update
sudo apt-get install git
sudo apt-get install libpcre3 libpcre3-dev

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
The following layout conventions are expected:

- virtualenv will be created into repo folder, so a corresponding entry in `.gitignore` file is recommended.
- requirements.txt is located into repo folder and contains python requirements for the server app

## clone git repository
```
git clone your_repo_url
```

## create virtual environment
Environment will be located inside the server app repo
```
cd your_repo
virtualenv --no-site-packages env
source env/bin activate
```

## update requirements
```
source env/bin activate
pip install -r requirements.txt
```


## give ownership to webserver user
```
chmod -R www-data .
```

## config templates variables
Templates are included for the various config files. 
They use Jinja template syntax, the following variables are required:

* `SERVER_APP_NAME`: app name (nginx, supervisor)
* `SERVER_APP_SOCKET_PATH`: path to socket for nginx <-> uwsgi communication (nginx, uwsgi)
* `SERVER_APP_SOCKET_PORT`: socket port to use for nginx <-> uwsgi communication (nginx, uwsgi, optional if `SERVER_APP_SOCKET_PATH` is not used)
* `SERVER_APP_DOMAIN`: app domain or ip to be served on (nginx)
* `SERVER_APP_MEDIA_FOLDER`: path do django media folder (ngix)
* `SERVER_APP_STATIC_FOLDER`: path to django static folder (nginx)
* `SERVER_APP_WSGI_PARAMS_PATH`:path to `uwsgi_params` file (nginx+uwsgi)

* `SERVER_APP_BASE_FOLDER`: base path of server app (uwsgi)
* `SERVER_APP_SYSTEM_USER`: user the webserver runs on (uwsgi)
* `SERVER_APP_VENV_PATH`: path to virtualenv (uwsgi)
* `SERVER_APP_UWSGI_INI_PATH`: path to `uwsgi.ini` (supervisor)



## uwsgi config
A sample uwsgi config for a django project is included in `uwsgi.ini.template` 


## nginx config
A sample nginx config for a django project is included in `nginx.conf.template`

`sudo ln -s /var/opt/ross-server/nginx/nginx.conf /etc/nginx/sites-enabled/ross-server.conf`

## supervisor config
Supervisor will be configured to:
* monitor nginx
* monitor uwsgi process

```
sudo ln nginx/supervisor.conf /etc/supervisor/conf.d/ross-server.conf
sudo supervisorctl reread
```

## bonus: postgresql
### installing
### enabling access from local machine



# template scripts

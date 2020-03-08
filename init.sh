#!/bin/bash

#DIR="/home/box/web"
DIR="/home/anton/data/src/python/web"

cd ${DIR}

NGINX_CONFIG="/etc/nginx/sites-enabled/default"
sudo rm "${NGINX_CONFIG}"
sudo ln -sf "${DIR}${NGINX_CONFIG}" "${NGINX_CONFIG}"
sudo /etc/init.d/nginx restart

gunicorn -c "${DIR}/hello.py" hello:app --daemon --bind 0.0.0.0:8080
${DIR}/ask/manage.py runserver 0.0.0.0:8000

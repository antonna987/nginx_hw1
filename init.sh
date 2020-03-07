#!/bin/bash

#DIR="/home/box/web"
DIR="/home/anton/data/src/python/web"

cd ${DIR}

NGINX_CONFIG="/etc/nginx/sites-enabled/default"
sudo rm "${NGINX_CONFIG}"
sudo ln -sf "${DIR}${NGINX_CONFIG}" "${NGINX_CONFIG}"
sudo /etc/init.d/nginx restart

GUNICORN_CONFIG="/etc/gunicorn.d/hello.py"
sudo rm "${GUNICORN_CONFIG}"
sudo rm "${DIR}/hello.py"
sudo ln -sf "${DIR}${GUNICORN_CONFIG}" "${GUNICORN_CONFIG}"
sudo ln -sf "${DIR}${GUNICORN_CONFIG}" "${DIR}/hello.py"
gunicorn -c "${GUNICORN_CONFIG}" hello:app

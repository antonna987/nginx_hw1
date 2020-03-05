#!/bin/bash

DIR="/home/box/web"
#DIR="/home/anton/data/src/python/web"

sudo rm "/etc/nginx/sites-enabled/default"
sudo ln -sf "${DIR}/etc/nginx/sites-enabled/default" "/etc/nginx/sites-enabled/default"
sudo /etc/init.d/nginx restart

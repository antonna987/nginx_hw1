#!/bin/bash
set -x

DIR=$1

sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database web_db;"

sudo mysql -uroot -e "create user box@localhost identified by '';"
sudo mysql -uroot -e "create user anton@localhost identified by '';"

sudo mysql -uroot -e "grant all privileges on web_db.* to box@localhost with grant option;"
sudo mysql -uroot -e "grant all privileges on web_db.* to anton@localhost with grant option;"

${DIR}/ask/manage.py makemigrations
${DIR}/ask/manage.py migrate

#!/bin/bash
echo "starting ******************************************************************"
echo "installing updates"
sudo apt-get update &&
sudo apt-get -y upgrade &&
echo "installing python"
sudo apt-get -y install python &&
echo "installing and upgrading pip"
sudo apt -y install python-pip &&
sudo python -m pip install --upgrade pip &&
echo "installing rabbitmq"
sudo apt -y install rabbitmq-server &&
echo "installing celery"
sudo python -m pip install celery &&
echo "installing openstack"
sudo python -m pip install python-openstackclient &&
echo "installing flask"
sudo apt -y install python-flask &&
echo "services ready, cloning repo"
sudo git clone https://github.com/nimaghoroubi/simple-service-cloud /simple-service-cloud &&
echo "clone complete! running services!"
sudo apt -y install screen
screen -dm python /simple-service-cloud/service.py &&
(cd /simple-service-cloud && screen -dm celery -A service.celery worker --loglevel=info)
echo "services up and running, use http://ip:5000/"
echo "ending ******************************************************************"

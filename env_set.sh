#!/bin/bash
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
sudo apt -y install python-flask
echo "*****************************/\*********************************"
celery --version
openstack --version
git clone https://github.com/nimaghoroubi/simple-service-cloud
screen python ~/simple-service-cloud/service.py

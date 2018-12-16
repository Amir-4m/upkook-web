#!/usr/bin/env bash

# Common dep.
sudo apt-get install -y build-essential ntp git
sudo apt-get install -y python-dev python-pip python3-dev python3-pip

# Setup memcached
sudo apt-get install -y memcached
sudo service memcached start

# Installing gnu gettext
sudo apt-get install -y gettext
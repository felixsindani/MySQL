#!usr/bin/env python3
'''installing MongoDB'''

wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list

sudo apt-get update

sudo apt-get install -y mongodb-org

sudo service mongod status

mongo --version

pip3 install pymongo

''' if documents creation doesn’t work or this error: Data directory /data/db not found., terminating'''

sudo mkdir -p /data/db

sudo service mongod start
#!/bin/bash
sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
cd /var/www/html
sudo yum install git -y
git clone https://github.com/andresbolivar19/MyRepo.git .

# Add script to mongodb
touche /etc/yum.repos.d/mongodb-org-3.0.repo

echo -e "[mongodb-org-3.0]" > /etc/yum.repos.d/mongodb-org-3.0.repo
echo -e "name=MongoDB Repository" >> /etc/yum.repos.d/mongodb-org-3.0.repo
echo -e "baseurl=https://repo.mongodb.org/yum/amazon/2013.03/mongodb-org/3.0/x86_64/" >> /etc/yum.repos.d/mongodb-org-3.0.repo
echo -e "gpgcheck=0" >> /etc/yum.repos.d/mongodb-org-3.0.repo
echo -e "enabled=1" >> /etc/yum.repos.d/mongodb-org-3.0.repo

sudo yum install -y mongodb-org

sudo service mongod start

sudo chkconfig mongod on

export LC_ALL=C

sed -e '/bindIp/ s/^#*/#/' -i /etc/mongod.conf

echo -e "db.createUser(" > /root/user.js
echo -e "{" >> /root/user.js
echo -e "user: "myUserAdmin"," >> /root/user.js
echo -e "pwd: "abc123"," >> /root/user.js
echo -e "roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]" >> /root/user.js
echo -e "}" >> /root/user.js
echo -e ")" >> /root/user.js

mongo < /root/user.js

service mongod restart

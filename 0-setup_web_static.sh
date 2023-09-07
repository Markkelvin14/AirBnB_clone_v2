#!/usr/bin/env bash
# sets up web servers for deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "working with web servers" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/
msg="location /hbnb_static/ {\nalias /data/web_static/current;\n}"
sudo sed -i "40i $msg" /etc/nginx/sites-enabled/default
sudo service nginx restart

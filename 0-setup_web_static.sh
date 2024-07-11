#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

# NGINX installation
if ! (command -v nginx >/dev/null 2>&1); then
    sudo apt-get -y update
    sudo apt-get install -y nginx
fi

# directory creation
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# creating new index.html file
var="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo -e "$var" > /data/web_static/releases/test/index.html

# create the symbolic link
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi

sudo ln -s /data/web_static/releases/test /data/web_static/current

# change of ownership and group to current user
sudo chown -R ubuntu:ubuntu /data/

# update the Nginx configuration to service specified content
position_pattern='^\tlocation \/ {'
nginx_conf_file="/etc/nginx/sites-available/default"
directive="location \/hbnb_static {\n\t\talias \/data\/web_static\/current;"

# Use grep to search for the directive in the nginx configuration file
if ! grep -qF "hbnb_static" "$nginx_conf_file"; then
    sed -i -e "/$position_pattern/{:1; /}/!{N;b1}; s|}|&\\n\t${directive}\n\t}|}" "$nginx_conf_file"
fi

# restart nginx
sudo service nginx restart

#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

# NGINX installation
if ! (command -v nginx >/dev/null 2>&1); then
    sudo apt-get -y update
    sudo apt-get install -y nginx
fi

# directory creation
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# creating new index.html file
echo -e "Hello Web Static!" > /data/web_static/releases/test/index.html

# create the symbolic link
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi

ln -s /data/web_static/releases/test /data/web_static/current

# change of ownership and group to current user
sudo chown -R ubuntu:ubuntu /data/

# update the Nginx configuration to service specified content
position_pattern="/^\tlocation \/hbnb_static {/"
match_pattern='^\s*root\s\+\S\+'
directive=$'\t\talias /data/web_static/current;'
nginx_conf_file="/etc/nginx/sites-available/default"

if ! grep -q "$directive" "$nginx_conf_file"; then
    if grep -q "$match_pattern" "$nginx_conf_file"; then
        sed -i "$position_pattern"',/^\s*}/ s|'"${match_pattern}|${directive}|" "$nginx_conf_file"
    else
        sed -i "$position_pattern"'a\ '"$directive" "$nginx_conf_file"
    fi
fi

# restart nginx
sudo service nginx restart

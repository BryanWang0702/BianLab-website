# BianLab-website
BianLab website, with Django + Bootstrap

# Installation
### Create enviroment
1. Install miniconda
```shell
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py38_4.9.2-Linux-x86_64.sh
chmod +x Miniconda3-py38_4.9.2-Linux-x86_64.sh
./Miniconda3-py38_4.9.2-Linux-x86_64.sh

# Refreash enviroment
source ~/.bashrc
```

2. Install mysql-5.7 and create a database for project
```shell
wget https://downloads.mysql.com/archives/get/p/23/file/mysql-server_5.7.39-1ubuntu18.04_amd64.deb-bundle.tar

tar -xvf mysql-server_5.7.39-1ubuntu18.04_amd64.deb-bundle.tar

# Update packages
sudo apt-get update
sudo apt-get upgrade
# Install necessary packages
sudo apt-get install libtinfo5
sudo apt-get -f install libmecab2

sudo dpkg -i mysql-common_5.7.39-1ubuntu18.04_amd64.deb
# Set a password for mysql
sudo dpkg-preconfigure mysql-community-server_5.7.39-1ubuntu18.04_amd64.deb
sudo dpkg -i libmysqlclient20_5.7.39-1ubuntu18.04_amd64.deb
sudo dpkg -i libmysqlclient-dev_5.7.39-1ubuntu18.04_amd64.deb
sudo dpkg -i libmysqld-dev_5.7.39-1ubuntu18.04_amd64.deb
sudo dpkg -i mysql-community-client_5.7.39-1ubuntu18.04_amd64.deb
sudo dpkg -i mysql-client_5.7.39-1ubuntu18.04_amd64.deb
sudo dpkg -i mysql-community-server_5.7.39-1ubuntu18.04_amd64.deb

# Finish mysql installation, try this command and enter the password you set
mysql -uroot -p

# Now you are in the mysql server, create a database
# The name of database(Here is bianlab) can be custom
create database bianlab;
```

3. Get source code and create a enviroment for code
```shell
git config --global user.name "YOURNAME"
git config --global user.email "YOUREMAIL"

# Clone the repository
git clone https://github.com/BryanWang0702/BianLab-website.git

# Create a enviroment with miniconda
# The name of enviroment(Here is bianlab) can be custom
conda create -n bianlab python=3.8

# Enter the project path and install the requirement packages of python
cd BianLab-website
pip install -r requirements.txt
```

4. Install nginx and configure
```shell
sudo apt-get install nginx -y
cd /etc/nginx
sudo vim nginx.conf

# The first line is "user www-data;"
# Modify it to "user ubuntu" or the user you are going to use to start the server.
# Save and quit (Check how to quit vim... This could be hard for beginner, Press ESC and enter :wq)

sudo vim sites-enabled/default

# Reset the server part 
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    # Ensure you can upload anything
    client_max_body_size 100;
    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        uwsgi_pass 127.0.0.1:8000;
        include /etc/nginx/uwsgi_params;
    }

    location /static {
        # Set to your project path, but remember to add a "/" in the end
        root /home/ubuntu/BianLab-website/;
    }

}
```

5. Install and configure the Uwsgi
```shell
# Install Uwsgi
conda install uwsgi

# To your project path, here is /home/ubuntu/BianLab-website
# Create the initialization file
vim uwsgi.ini

# Add these 
[uwsgi]
socket=127.0.0.1:8000

chdir=/home/ubuntu/BianLab-website

wsgi-file=BianLab-website/wsgi.py

master=true

process=32

thread=4

pidfile=uwsgi.pid

daemonize=uwsgi.log

# Quit uwsgi.ini and save

```

# Configure
1. Set the `settings.py` in `BianLab-website/bianweb_v2`
```shell
vim bianweb_v2/settings.py

# Change the database and password to yours in line 95 and 96
# Save and quit

```
2. Move the data into mysql server
```shell
# Migrate data
python manage.py makemigrations
python manage.py migrate

# Collect static files
python manage.py collectstatic
```

3. Create a superuser to manager the website
```shell
python manage.py createsuperuser
```

4. Start the server
```shell
systemctl start nginx
uwsgi --ini uwsgi.ini
```

5. Now you can check your site!

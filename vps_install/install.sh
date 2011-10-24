screen -S installsystem
sudo su
cp /etc/apt/sources.list /etc/apt/sources.list.bak
dpkg-reconfigure locales

echo "" > /etc/apt/sources.list
echo "deb http://http.us.debian.org/debian/ testing main non-free contrib" >> /etc/apt/sources.list
echo "deb-src http://http.us.debian.org/debian/ testing main non-free contrib" >> /etc/apt/sources.list
apt-get update
aptitude update
apt-get upgrade
aptitude upgrade

aptitude install gcc nginx mysql-client mysql-server
aptitude install spawn-fcgi
aptitude install python-webpy python-mysqldb 
aptitude install php5 php5-fpm php5-mysql

# set beijing date
cp /etc/localtime /etc/localtime.bak
rm -rf /etc/localtime
ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

rm /etc/nginx/sites-enabled/default
cp /etc/php5/fpm/pool.d/www.conf /etc/php5/fpm/pool.d/www.conf.bak
cp conf/php5-fpm-www-conf /etc/php5/fpm/pool.d/www.conf
/etc/init.d/nginx restart
/etc/init.d/php5-fpm restart


# exit screen
exit

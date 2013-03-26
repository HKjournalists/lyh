aptitude update
aptitude install screen
screen -S installsystem




cp /etc/apt/sources.list /etc/apt/sources.list.bak
aptitude install locales
dpkg-reconfigure locales

echo "" > /etc/apt/sources.list
echo "deb http://debian.ustc.edu.cn/debian/ testing main non-free contrib" >> /etc/apt/sources.list
echo "deb-src http://debian.ustc.edu.cn/debian/ testing main non-free contrib" >> /etc/apt/sources.list
echo "deb http://debian.ustc.edu.cn/debian/ sid main non-free contrib" >> /etc/apt/sources.list
apt-get update
aptitude update
apt-get upgrade
aptitude upgrade

aptitude install git gcc nginx mysql-client mysql-server spawn-fcgi
aptitude install python-webpy python-mysqldb python-setuptools python-imaging python-httplib2 python-memcache
easy_install pip
aptitude install php5 php5-fpm php5-mysql
aptitude install sphinxsearch imagemagick memcached heirloom-mailx exim4
aptitude install curl vnstat vim zsh unzip dstat telnet ntpdate
aptitude install vim-gnome vim-gui-common vim-full
ntpdate 210.72.145.44

# set beijing date
cp /etc/localtime /etc/localtime.bak
rm -rf /etc/localtime
ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

rm /etc/nginx/sites-enabled/default
cp /etc/php5/fpm/pool.d/www.conf /etc/php5/fpm/pool.d/www.conf.bak
cp conf/php5-fpm-www-conf /etc/php5/fpm/pool.d/www.conf
cp conf/close_default /etc/nginx/sites_enabled/
/etc/init.d/nginx restart
/etc/init.d/php5-fpm restart

echo "SET time_zone = '+8:00'" | mysql -uroot -p131400

echo "ok"

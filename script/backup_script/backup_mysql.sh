#!/bin/bash
set -e

ssh -o "ServerAliveInterval 300" sdjl@lengxiaohua3 '/home/sdjl/mysql_backup/backup.sh'
cd /home/sdjl/backup/mysql_lengxiaohua3
git pull origin master

ssh -o "ServerAliveInterval 300" sdjl@lengxiaohua2 '/home/sdjl/mysql_backup/backup.sh'
cd /home/sdjl/backup/mysql_lengxiaohua2
git pull origin master

ssh -o "ServerAliveInterval 300" sdjl@aoaola '/home/sdjl/mysql_backup/backup.sh'
cd /home/sdjl/backup/mysql_aoaola
git pull origin master

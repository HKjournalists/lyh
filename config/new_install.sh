#!/bin/bash
if [ "x$(whoami)" != "xroot" ]; then
    echo "Only root can run this script."
    exit 1
fi

echo "install mysql"
aptitude install mysql-client mysql-server python-mysqldb

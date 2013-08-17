#!/usr/bin/env sh

set -e

sudo ifconfig lo0 add 127.0.0.10/32
sudo ipfw add fwd 127.0.0.10,8080 tcp from any to 127.0.0.10 80
sudo ipfw add fwd 127.0.0.10,2222 tcp from any to 127.0.0.10 22

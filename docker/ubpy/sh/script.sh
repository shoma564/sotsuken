#!/bin/bash

touch /etc/result1.txt
chmod 777 /etc/result1.txt
cp /etc/result1.txt /etc/share/


python3 /etc/sc.py

/usr/sbin/sshd -D

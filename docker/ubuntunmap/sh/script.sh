#!/bin/bash

touch /etc/nmap.txt
touch /etc/result.txt

chmod 777 /etc/nmap.txt
chmod 777 /etc/result.txt

nmap -T4 -A 1873237429 >> /etc/nmap.txt
grep 'tcp' /etc/nmap.txt > /etc/result.txt
cat /etc/result.txt
cp /etc/result.txt /etc/share/

/usr/sbin/sshd -D

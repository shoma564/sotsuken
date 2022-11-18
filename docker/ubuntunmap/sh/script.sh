#!/bin/bash

rm nmap.txt
rm result.txt
touch /etc/nmap.txt
touch /etc/result.txt

chmod 777 /etc/nmap.txt
chmod 777 /etc/nmap.txt

nmap -T4 -A 172.24.20.126 >> /etc/nmap.txt
grep 'tcp' /etc/nmap.txt > /etc/result.txt
cat result.txt




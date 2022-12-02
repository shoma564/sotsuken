#!/bin/bash
docker-compose down

docker-compose down --rmi all --volumes --remove-orphans
docker build ./ubpy -t shomaigu/sotsuken-python:latest
docker push shomaigu/sotsuken-python:latest
docker build ./ubuntuman -t shomaigu/sotsuken-ubuntu-manage:latest
docker push shomaigu/sotsuken-ubuntu-manage:latest
docker build ./ubuntunmap -t shomaigu/sotsuken-ubuntu-nmap:latest
docker push shomaigu/sotsuken-ubuntu-nmap:latest

docker-compose build
docker-compose up

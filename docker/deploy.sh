#!/bin/bash
docker-compose down
docker-compose down --rmi all --volumes --remove-orphans


docker build ./python -t shomaigu/sotsuken-pysc:latest
docker push shomaigu/sotsuken-pysc:latest
docker-compose up

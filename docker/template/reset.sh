#!/bin/bash
cd `dirname $0`
rm  ../share/*
cp -f ./ubuntunmap/sh/script.sh ../ubuntunmap/sh/script.sh
cp -f ./ubpy/python_hon/sc.py ../ubpy/python_hon/sc.py
docker-compose down
docker system prune

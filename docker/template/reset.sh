#!/bin/bash
cd `dirname $0`
rm  ../share/result.txt
rm  ../share/result1.txt
cp ./ubuntunmap/sh/script.sh ../ubuntunmap/sh/script.sh
cp ./ubpy/python_hon/sc.py ../ubpy/python_hon/sc.py
docker-compose down
docker system prune

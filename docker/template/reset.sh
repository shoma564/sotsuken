#!/bin/bash
cd `dirname $0`
rm  ../share/result.txt
rm  ../share/result1.txt
cp ./ubuntunmap/sh/script.sh ../ubuntunmap/sh/script.sh
docker-compose down
docker system prune

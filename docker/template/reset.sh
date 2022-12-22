#!/bin/bash
cd `dirname $0`
rm  ../share/result.txt
cp ./ubuntunmap/sh/script.sh ../ubuntunmap/sh/script.sh
docker-compose down

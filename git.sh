#!/bin/bash
while true
do
  today=`date "+%Y%m%d"`
  git add *
  git commit -m '自動プッシュ ${today}'
  git push
  sleep 600
done

#!/bin/bash
while true
do
  kai=0
  today=`date "+%Y%m%d"`
  mozi="自動プッシュ"
  su="回目のプッシュ完了"
  git add *
  git commit -m '${mozi} ${today}'
  git push
  echo $kai$su
  sleep 600
done

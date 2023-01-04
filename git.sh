#!/bin/bash
cd `dirname $0`

while true
do
  kai=1
  today=`date "+%Y%m%d%k%M"`
  mozi="自動プッシュ"
  su="回目のプッシュ完了"
  echo ${mozi} ${today}
  git remote add origin git@github.com:shoma564/sotsuken.git
  git remote -v
  git checkout main
  git add /home/shoma/sotsuken/*
  git commit -m "${today}"
  git push
  echo $kai$su
  kai=kai+1
  sleep 1200
done


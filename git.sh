#!/bin/bash
while true
do
  kai=1
  today=`date "+%Y%m%d%k%M"`
  mozi="自動プッシュ"
  su="回目のプッシュ完了"
  echo ${mozi} ${today}
  ssh-add -K ~/.ssh/id_rsa
  git checkout main
  git add /home/shoma/sotsuken/*
  git commit -m "${today}"
  git push main
  echo $kai$su
  kai=kai+1
  sleep 1200
done

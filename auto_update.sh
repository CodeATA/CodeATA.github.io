#!/bin/bash

rt_dir=/root/CodeATA.github.io
spider_dir=$rt_dir/recharge

cd $spider_dir

git pull

/usr/local/bin/scrapy crawl tb_recharge
mv $spider_dir/a.out $rt_dir
$rt_dir/update_csv.py $rt_dir
#rm $rt_dir/a.out

timestamp=$(date +"%Y-%m-%d %H:%M:%S")
cd $rt_dir
#echo $timestamp >> test.txt
git commit -a -m "$timestamp update"
#git commit -a -m "test crontab git"
git push

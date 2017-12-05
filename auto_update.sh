#!/bin/bash

rt_dir=/home/cdw/CodeATA.github.io/
spider_dir=$rt_dir/recharge

cd $spider_dir
PATH=$PATH:/usr/local/bin
export PATH
scrapy crawl tb_recharge
mv $spider_dir/a.out $rt_dir
$rt_dir/update_csv.py $rt_dir
rm $rt_dir/a.out

timestamp=$(date +"%Y-%m-%d %H:%M:%S")
git commit -a -m "$timestamp update"
git push

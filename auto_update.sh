#!/bin/bash

rt_dir=/home/cdw/CodeATA.github.io/
spider_dir=$rt_dir/recharge

cd $spider_dir
scrapy crawl tb_recharge
mv $spider_dir/a.out $rt_dir
$rt_dir/update_csv.py
rm $rt_dir/a.out

timestamp=$(date +"%Y-%m-%d %H:%m:%S")
git commit -a -m "$timestamp update"
git push

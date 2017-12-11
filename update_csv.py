#!/usr/bin/python3
# -*- coding: <utf-8> -*-

import csv
import re
import datetime
import sys

shops = {'530539251218':'欧石晶坊',
         '526087187883':'黑兔充值',
         '544562937140':'手游专业充值平台',
         '528263080941':'小埋小店果冻君小店',
         '543831356367':'老狼手游充值',
         '549931060579':'业务君的小店',
         '526391288719':'柯基家',}
row = {'date':'',
       'time':'',
       '欧石晶坊':'',
       '黑兔充值':'',
       '手游专业充值平台':'',
       '小埋小店果冻君小店':'',
       '老狼手游充值':'',
       '业务君的小店':'',
       '柯基家':'',}

rt_dir = sys.argv[1]
price_name = rt_dir+'/a.out'
csv_name = rt_dir+'/fgo-price.csv'

with open(price_name, 'r') as price_file:
    for line in price_file:
        id_price = re.split(',|\n', line)
        row[shops[id_price[0]]] = id_price[1]

today = datetime.datetime.now()
date = today.strftime('%Y-%m-%d')
time = today.strftime('%H:%M:%S')

row['date'] = date
row['time'] = time

with open(csv_name, 'a', newline='') as csvfile:
    fieldnames=['date', 'time', '欧石晶坊', '黑兔充值', '手游专业充值平台', '小埋小店果冻君小店', '老狼手游充值', '业务君的小店', '柯基家']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow(row)






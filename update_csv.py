#!/usr/bin/python3
# -*- coding: <utf-8> -*-

import csv
import re
import datetime

shops = {'530539251218':'欧石晶坊',
         '526087187883':'黑兔充值',
         '544562937140':'手游专业充值平台',
         '528263080941':'小埋小店果冻君小店',
         '543831356367':'老狼手游充值',
         '549931060579':'业务君的小店',
         '526391288719':'柯基家',}
row = {'date':'',
       '欧石晶坊':'',
       '黑兔充值':'',
       '手游专业充值平台':'',
       '小埋小店果冻君小店':'',
       '老狼手游充值':'',
       '业务君的小店':'',
       '柯基家':'',}

with open('a.out', 'r') as price_file:
    for line in price_file:
        id_price = re.split(',|\n', line)
        row[shops[id_price[0]]] = id_price[1]

today = datetime.datetime.now()
date = today.strftime('%Y-%m-%d')
time = today.strftime('%H:%M:%S')
print(date)
print(time)

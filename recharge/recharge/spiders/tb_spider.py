# -*- coding: <utf-8> -*-

import scrapy
import re

class Spider(scrapy.Spider):
    name = "tb_recharge"
    urls = ['https://item.taobao.com/item.htm?spm=a230r.1.14.19.448e0757ptgTZM&id=530539251218',
            'https://item.taobao.com/item.htm?spm=a230r.1.14.57.448e0757ptgTZM&id=526087187883',
            'https://item.taobao.com/item.htm?spm=a230r.1.14.51.448e0757ptgTZM&id=544562937140',
            'https://item.taobao.com/item.htm?spm=a230r.1.14.26.448e0757ptgTZM&id=528263080941',
            'https://item.taobao.com/item.htm?spm=a230r.1.14.32.448e0757ptgTZM&id=543831356367',
            'https://item.taobao.com/item.htm?spm=a230r.1.14.38.448e0757ptgTZM&id=549931060579',
            'https://item.taobao.com/item.htm?spm=a1z10.1-c.w4004-7398620829.21.5304a160Xh4s20&id=526391288719',]


    def start_requests(self):    
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        shop_id = re.match(r'.*\&id=(.*)', response.url).group(1)
        
        price = response.xpath('//strong[@id="J_StrPrice"]/em[@class="tb-rmb-num"]/text()').extract()[0]
        with open("a.out", "a") as f:
            f.write(shop_id+','+price+'\n')

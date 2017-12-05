# -*- coding: <utf-8> -*-

import scrapy
import re
import scrapy_splash 


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
            yield scrapy_splash.SplashRequest(url=url, callback=self.parse,
                args={'wait':10,}
            )

    def parse(self, response):
        shop_id = re.match(r'.*\&id=(.*)', response.url).group(1)
        #page = shop_id+'.html'
        #with open(page, 'wb') as page_file:
        #    page_file.write(response.body)

        ori_price = response.xpath('//li[@id="J_StrPriceModBox"]//em[@class="tb-rmb-num"]/text()').extract()[0]
        promo_price_list = response.xpath('//li[@id="J_PromoPrice"]//em[@id="J_PromoPriceNum"]/text()').extract()
        if promo_price_list:
            price = promo_price_list[0]
            #print("\npromo!\n")
        else:
            price = ori_price
        with open("a.out", "a") as f:
            f.write(shop_id+','+price+'\n')
        

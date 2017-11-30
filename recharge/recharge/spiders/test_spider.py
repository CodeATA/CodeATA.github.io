import scrapy
import re

class Spider(scrapy.Spider):
    name = "tb_recharge"
    urls = [
            'https://item.taobao.com/item.htm?spm=a230r.1.14.19.448e0757ptgTZM&id=530539251218',
            'https://item.taobao.com/item.htm?spm=a230r.1.14.57.448e0757ptgTZM&id=526087187883',
            'https://item.taobao.com/item.htm?spm=a230r.1.14.51.448e0757ptgTZM&id=544562937140',
            'https://item.taobao.com/item.htm?spm=a230r.1.14.26.448e0757ptgTZM&id=528263080941',
            'https://item.taobao.com/item.htm?spm=a230r.1.14.32.448e0757ptgTZM&id=543831356367',
            'https://item.taobao.com/item.htm?spm=a230r.1.14.38.448e0757ptgTZM&id=549931060579',
            'https://item.taobao.com/item.htm?spm=a1z10.1-c.w4004-7398620829.21.5304a160Xh4s20&id=526391288719',
            ]

    def start_requests(self):    
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)
        print("finish here")

    def parse(self, response):
        #page = response.url.split("/")[-2]
        #page = self.urls[response.url]
        res = re.match(r'.*\&id=(.*)', response.url)
        filename = res.group(1)+'.html'
        for line in response.body:
            line_match = re.match(r'<strong id=\"J_StrPrice\"><em class=\"tb-rmb\">\&yen\;</em><em class=\"tb-rmb-num\">(.*)</em></strong>', line)
            if line_match:
                price = line_match.group(1)
        with open(filename, 'wb') as f:
            f.write(price)
        self.log('Saved file %s' % filename)

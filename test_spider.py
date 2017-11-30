import scrapy

class Spider(scrapy.Spider):
    name = "test"

    def start_requests(self):
        urls = ['https://item.taobao.com/item.htm?spm=a230r.1.14.19.448e0757ptgTZM&id=530539251218&ns=1&abbucket=10#detail']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #page = response.url.split("/")[-2]
        filename = 'test.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

import scrapy

from girl.items import GirlItem

class girlSpider(scrapy.Spider):
    name='Girl'
    allowed_domains=['http://www.ivsky.com/']
    start_urls=[
        'http://www.ivsky.com/tupian/ziranfengguang/'
    ]
    def parse(self,response):
        list = response.css(".ali li")
        for img in list:
            # print()
            base_url = 'http://www.ivsky.com'
            imgname = img.css("a::attr(title)").extract_first()
            imgurl = img.css("a::attr(href)").extract_first()
            imgurl2= base_url + imgurl
            print(imgname)
            print(imgurl2)
            # next_url=
    #         yield scrapy.Request(imgurl2,callback=self.content)
    # def content(self,response):

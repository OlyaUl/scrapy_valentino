import scrapy
# import ValentinoProduct
#from valentino.items import ValentinoProduct
# import valentino.items.ValentinoPrice
from valentino.items import ValentinoProduct


class mySpider(scrapy.Spider):
    name = 'valent'
    allowed_domains = []
    # start_urls = ['https://www.valentino.com']
    custom_settings = []

    def __init__(self, url="https://www.valentino.com/", *args, **kwargs):
        self.url = url
        super(mySpider, self).__init__(mySpider, *args, **kwargs)

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        # search_url = "https://www.valentino.com/{}".format('ua/shop/для-женщин/прет-а-порте/рубашки-и-топы#')
        search_url = "https://www.valentino.com/ua/shop/%D0%B4%D0%BB%D1%8F-%D0%B6%D0%B5%D0%BD%D1%89%D0%B8%D0%BD/%D0%BF%D1%80%D0%B5%D1%82-%D0%B0-%D0%BF%D0%BE%D1%80%D1%82%D0%B5/%D0%BF%D0%BB%D0%B0%D1%82%D1%8C%D1%8F#"
        # response
        yield scrapy.Request(url=search_url, callback=self.result_parse,
                             dont_filter=True, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/56.0'}, meta={'category': []})

    # def parse.items
    # yield item
    # def parse.page
    # def parse.detail

    def result_parse(self, response):
        res = response.xpath("/ul/li/a//text()").extract()
        prod = ValentinoProduct()
        # prod.name = 'test'
        # res = response.body
        print(res)







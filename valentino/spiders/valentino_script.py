import scrapy
from valentino.items import ValentinoProduct


class MySpider(scrapy.Spider):
    name = 'valent'
    allowed_domains = []
    # start_urls = ['https://www.valentino.com']
    custom_settings = []

    def __init__(self, url="https://www.valentino.com/", *args, **kwargs):
        self.url = url
        super(MySpider, self).__init__(MySpider, *args, **kwargs)

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        search_url = "https://www.valentino.com/{}".format('ua/shop/для-женщин/прет-а-порте/')
        # response
        yield scrapy.Request(url=search_url, callback=get_categories,
                             dont_filter=True,
                             headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                                                    '(KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'},
                             meta={'categories': []})


def get_categories(response):
    categories = response.xpath('//ul[@class="level-2"]/li[@id="donna_categories_abbigliamento"]/'
                                'ul[@class="level-3"]/li/a')
    for category in categories:
        url_cat = category.xpath('@href').extract_first()
        name_cat = category.xpath('span/text()').extract_first()
        print(name_cat)
        response.meta['categories'].append(name_cat)
        # prod = ValentinoProduct()
        # prod.categories = category_name
        yield scrapy.Request(
            url=url_cat,
            callback=get_items,
            meta={
                'categories': response.meta['categories'],
            }
        )


def get_items(response):
    # print(response.body)
    items = response.xpath('//section[@class="search"]/ul[@class="products"]/li[@class="item"]/'
                           'article[@class="search-item"]/header/a')
    print(items)
    for item in items:
        print(item)
        url = item.xpath('@href').extract_first()
        name = item.xpath('title').extract_first()
        print(name, url)
        yield scrapy.Request(
            url=url,
            callback=get_items)




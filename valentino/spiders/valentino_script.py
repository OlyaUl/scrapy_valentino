import scrapy
from datetime import date

from valentino.items import ValentinoProduct, ValentinoPrice


class MySpider(scrapy.Spider):
    name = 'valent'
    allowed_domains = []
    # start_urls = ['https://www.valentino.com']
    custom_settings = []

    '''def __init__(self, url='https://www.valentino.com/ua/shop/для-женщин/прет-а-порте/', *args, **kwargs):
        self.url = url
        super(MySpider, self).__init__(MySpider, *args, **kwargs)
        self.url = url'''

    def __init__(self, url="https://www.valentino.com/", *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.url = url


    def start_requests(self):
        yield scrapy.Request(url=self.url,
                             callback=self.get_categories,
                             headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                                                    '(KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'},)

    def get_categories(self, response):
        categories = response.xpath('//ul[@class="level-2"]/li[@id="donna_categories_abbigliamento"]/'
                                    'ul[@class="level-3"]/li/a')
        for category in categories:
            meta = {}
            id = 0
            url_cat = category.xpath('@href').extract_first()
            name_cat = category.xpath('span/text()').extract_first()
            print(name_cat)
            meta['categories'] = name_cat
            yield scrapy.Request(
                url=url_cat,
                callback=self.get_items,
                meta=meta
            )

    def get_items(self, response):
        items = response.xpath('//ul[@class="products "]/li[@class="item "]/article/div[@class="search-item-info"]/span/a')        #print(items)
        i = 0
        for item in items:
            i = i+1
            url = item.xpath('@href').extract_first()
            yield scrapy.Request(
                url=url,
                callback=self.get_item, meta=response.meta)

    def get_item(self, response):
        product = ValentinoProduct()
        price = ValentinoPrice()
        product['name'] = response.xpath(
            '//h1[@class="item-name"]/div/span[@class="value"]/text()'
        ).extract_first()#.strip()
        print(product['name'])

        # product['site_product_id'] = response.id

        product['model'] = response.xpath(
            '//div[@class="modelName outer"]/span[@class="inner modelName"]/text()'
        ).extract_first()  # .strip()

        product['category'] = response.meta['categories']

        product['description'] = response.xpath(
            '//div[@class="attributesUpdater editorialdescription "]/span[@class="value"]'
        ).extract_first()  # .strip()
        print(product['description'])

        product['url'] = response.url

        product['image'] = response.css('div.mainImage ul.alternativeImages img::attr(srcset)').extract()

        product['site'] = 'https://www.valentino.com/'
        print(product)
        yield product

        price['currency'] = '€'
        price1 = response.xpath('//div[@class="item-price"]//span[@class="price"]/'
                               'span[@class="value"]/text()').extract_first()
        if not price1:
            price1 = response.xpath('//div[@class="item-price"]//span[@class="full price"]/'
                                   'span[@class="value"]/text()').extract_first()
        sale_price1 = response.xpath('//div[@class="item-price"]//span[@class="discounted price"]'
                                    '/span[@class="value"]/text()').extract_first()
        size1 = response.css('div.item-sizeSelection span.sizeValue::text').extract()
        price['params'] = {
            'price' :price1,
            'size': size1,
            'sale_price': sale_price1

        }
        print(price)
        yield price

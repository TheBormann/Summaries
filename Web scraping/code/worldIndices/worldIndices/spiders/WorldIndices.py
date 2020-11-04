import scrapy
from ..items import IndexItem
from scrapy.loader import ItemLoader


class WorldIndices(scrapy.Spider):
    name = "WorldIndices"
    start_urls = [
        "https://www.investing.com/indices/world-indices"
    ]
    allowed_domains = ["https://www.investing.com/indices"]

    # scrapy shell "https://www.investing.com/indices/world-indices" -s USER_AGENT='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'

    def parse(self, response):
        for country in range(1, 93):
            for index in response.xpath('//*[@id="leftColumn"]/table[' + str(country) +']/tbody/tr'):

                loader = ItemLoader(item=IndexItem(), selector=index)
                loader.add_xpath("country", '//*[@id="leftColumn"]/h2[' + str(country) + ']/a/text()')
                loader.add_xpath("index", './td[2]/a/text()')
                loader.add_xpath("last", './td[3]/text()')
                loader.add_xpath("high", './td[4]/text()')
                loader.add_xpath("low", './td[5]/text()')
                loader.add_xpath("changeTotal", './td[6]/text()')

                index_item = loader.load_item()
                yield index_item

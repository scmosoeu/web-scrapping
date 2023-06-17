import scrapy


class PricesSpider(scrapy.Spider):
    name = "prices"
    allowed_domains = ["ctmarket.co.za"]
    start_urls = ["https://ctmarket.co.za"]

    def parse(self, response):
        pass

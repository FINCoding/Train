import scrapy

class ToursSpider(scrapy.Spider):
    def start_requests(self):
        urls = [
            'https://www.onlinetours.ru/',

        ]
import scrapy

class SportSpider(scrapy.Spider):
    name = 'sport_articles'
    
    def start_requests(self):
        urls = [
            'https://news.sportbox.ru/',
            'https://news.sports.ru/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[2]
        filename = 'articles-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
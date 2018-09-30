import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/3/',
            'http://quotes.toscrape.com/page/4/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'quotes.txt'
        with open(filename, 'wb') as f:
            for quote in response.css("div.quote"):
                text = quote.css("span.text::text").extract_first()
                author = quote.css("small.author::text").extract_first()
                tags = quote.css("div.tags a.tag::text").extract()
                print(dict(text=text, author=author, tags=tags))

        # page = response.url.split("/")[-2]
        # filename = 'quotes%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.css('quote'))
            # f.write(response.body)
        # self.log('Saved file %s' % filename)

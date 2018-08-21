from pyspider.libs.base_handler import *

class Handler(BaseHandler):

    @every(minutes=24*60)
    def on_start(self):
        self.crawl('https://tproger.ru/tag/python/', callback=self.index_page)

    @config(age=10*24*60*60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return{
            "url": response.url,
            "title": response.doc('title').text(),
        }

if __name__ == '__main__':
    a = Handler()
    a.on_start()
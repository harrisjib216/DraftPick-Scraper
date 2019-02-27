import scrapy

class BlogSpider(scrapy.Spider):
    # project
    name = 'blogspider'

    # scrape data
    def parse(self, url):
        data = []
        for title in url.css('.post-header>h2'):
            data.append({'title': title.css('a ::text').get()})

        print(data)

    
    # begin program
    def start_scraping(self):
        print "hello"
        urls = ['https://blog.scrapinghub.com']
        for url in urls:
            scrapy.Request(url=url, callback=self.parse(url))


# begin
my_scrape = BlogSpider(scrapy.Spider)
my_scrape.start_scraping()
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "tripadvisor"
    start_urls = [
        'https://www.tripadvisor.com/Restaurants-g294074-Bogota.html',
    ]

    def parse(self, response):
        for restaurant in response.css("a._15_ydu6b"):
            yield {
                'name': restaurant.get(),
                'url': restaurant.attrib['href']
            }

        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
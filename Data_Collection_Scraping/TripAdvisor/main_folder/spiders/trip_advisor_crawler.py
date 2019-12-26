# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TripAdvisorCrawlerSpider(CrawlSpider):
    name = 'trip_advisor_crawler'
    allowed_domains = ['www.tripadvisor.it']

    # this is to set up the user agent variable (I can check my user agent my typing it inside my browser)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

    # this block overwrites the static request method 
    # n.b in the crawl spider I do not need to specify the callback method inside the request
    def start_requests(self):
        yield scrapy.Request(url='https://www.tripadvisor.it/Restaurants-g187791-Rome_Lazio', headers={
            'User-Agent': self.user_agent
        })

    rules = (
        # the link extractor specifies the link I want to extract 
        # each rule is responsable to follow certain links

        # the first rule selects all the 50 movies there are on the starting page
        # I do not need to speficy the @href inside the xpath expression because it is selected automatically 
        # the process_request method serves to change the user agent each time I access a movie link
        Rule(LinkExtractor(restrict_xpaths="//div[@class='restaurants-list-ListCell__nameBlock--1hL7F']/span/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
        # the second rule selects the next page button so that I can change the page when I finish retrieving all the movies on the page selected by the first rule above
        # the process_request method serves to change the user agent each time I access a movie link
        Rule(LinkExtractor(restrict_xpaths="//div[@class='unified pagination js_pageLinks']/a[@class='nav next rndBtn ui_button primary taLnk']"), process_request='set_user_agent')
    )

    # this block defines the user agent for the request
    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request


    def parse_item(self, response):
        yield {
            # these features are extracted from the link selected by the first rule line (with the first rule I open the link and then I extract all the features I need)
            'title': response.xpath("//h1[@class='ui_header h1']/text()").get(),
            'icon_prize': response.xpath("//div[@class='header_links']/a[@href='/Restaurants-g187791-Rome_Lazio.html?pid=6']/text()").get(),
            'average_price': response.xpath("//div[@class='restaurants-detail-overview-cards-DetailsSectionOverviewCard__detailsSummary--evhlS']/div/div[2]/text()").get(),
            'users_rate': response.xpath("//span[@class='restaurants-detail-overview-cards-RatingsOverviewCard__overallRating--nohTl']/text()").get(),
            'number_reviews': response.xpath("//div[@class='restaurants-detail-overview-cards-RatingsOverviewCard__primaryRatingRow--VhEsu']/a[@href='#REVIEWS']/text()").get(),
            'street': response.xpath("//span[@class='street-address']/text()").get()

        }

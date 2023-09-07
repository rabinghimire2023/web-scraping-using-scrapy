"""
Web Scraping using Scrapy.
"""
import scrapy

class QuotesSpider(scrapy.Spider):
    """
    Class to Scrape the quotes and authores using Scrapy.

    Yields:
        quotes: The quotes from the page.
        author: The name of the authore
    """
    name = 'quotes_spider'
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'quotes': quote.css('span.text::text').get(),
                'author': quote.css('span small.author::text').get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

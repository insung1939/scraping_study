import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes" # spider name
    allowed_domains = ["quotes.toscrape.com"]   # crawling domain
    start_urls = ["http://quotes.toscrape.com/"] # starting webpage

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "quote": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        # move to next page (Pagination)
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

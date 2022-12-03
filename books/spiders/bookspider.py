from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from books.items import BookItem

class BookSpider(CrawlSpider):
    name = "Books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_css=".nav-list > li > ul > li > a"), follow=True),
        Rule(LinkExtractor(restrict_css=".product_pod > h3 > a"), callback="parse_book")
    )

    def parse_book(self, response):
        book_item = BookItem()
        book_item["title"] = response.css(".col-sm-6.product_main > h1::text").get()
        book_item["price"] = response.css(".price_color::text").get()
        book_item["upc"] = response.css(".table.table-striped > tr:nth-child(1) > td::text").get()
        book_item["availability"] = response.css(".table.table-striped > tr:nth-child(6) > td::text").get()
        book_item["url"] = response.url

        return book_item

# ITE College West Python elective Project Scenario 2, group 13.
import scrapy
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['https://ite.edu.sg/']
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

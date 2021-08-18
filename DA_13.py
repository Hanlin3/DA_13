# ITE College West Python elective Project Scenario 2, group 13.
# Important!! To get PyCharm to run this thing I had to do this, otherwise exit status 0 after click on play button!!:
# - Go into edit configurations. Inside of it, click on "Script Path", change to "Module Name".
# - Module Name: scrapy.cmdline
# - Parameters: runspider DA_13.py
# Notes:: After you done modifications, under "changes" click tick box then press the commit and push... Thanks!

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
q
# ITE College West Python elective project. [Scenario 2 group 13]
# Note: To get PyCharm to run this scrapy script:
# - Go into edit configurations. Inside of it, click on "Script Path", change it to "Module name".
# - Module name: scrapy.cmdline
# - Parameters: runspider DA_13.py
# Note: After you've made modifications, under "Commit to master", tick the "Changes" box and then click "Commit and Push...".

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


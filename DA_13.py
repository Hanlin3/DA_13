# ITE College West Python elective project. [Scenario 2 group 13]
# Note: To get PyCharm to run this scrapy script:
# - In pycharm venv terminal, pip install scrapy
# - In pycharm venv terminal, pip install requests
# - Go into edit configurations. Inside of it, click on "Script Path", change it to "Module name".
# - Module name: scrapy.cmdline
# - Parameters: runspider DA_13.py -s USER_AGENT="Anything"
# Note: After you've made modifications, click on Git > Commit...
# Under "Commit to master", tick the "Changes" box and then click "Commit and Push...".
# To output as JSON file, paste this in venv terminal: scrapy runspider DA_13.py -s USER_AGENT="Anything" -o test.json -t json

import scrapy
import requests

##changing parts***********************************************************

# url for group13
url = "https://brickset.com/sets/year-2010"
r = requests.get(url)
print(r.text)


# Display an OK return status (task5.ii
print("Status code:")
print("\t*",r.status_code)


# Display the Website Hearder (task5.iii
h = requests.head(url)
print("Header:")
print("**********")
for x in h.headers:
    print("\t",x,".",h.headers[x])
print("**********")


# Modify the Header user-agent to display "Mobile" (task5.iv
headers = {
    'User-Agent' : 'Mobile'
}
r2 = requests.get(url,headers=headers)
print(r2.request.headers)

##changing parts***********************************************************




class BrickSetSpider(scrapy.Spider):
    name = 'brick_spider'
    start_urls = ['https://brickset.com/sets/year-2010']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h1 ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

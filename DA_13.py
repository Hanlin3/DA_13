# ITE College West Python elective project. [Scenario 2 group 13]
# Note: To get PyCharm to run this scrapy script:
# - Go into edit configurations. Inside of it, click on "Script Path", change it to "Module name".
# - Module name: scrapy.cmdline
# - Parameters: runspider DA_13.py -s USER_AGENT="DigitalOcean Tutorial"
# Note: After you've made modifications, click on Git > Commit...
# Under "Commit to master", tick the "Changes" box and then click "Commit and Push...".

import scrapy
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest


class TASK5():
    def task5_1(self):
        # Request the get
        url = "https://brickset.com/sets/year-2010"
        r = requests.get(url)
        #print(r.text)
    
    def task5_2(self):
        # Display an OK return status (task5.ii
        print("Status code:")
        print("\t*",r.status_code)
        
    def task5_3(self):
        # Display the Website Hearder (task5.iii
        h = requests.head(url)
        print("Header:")
        print("**********")
        for x in h.headers:
            print("\t",x,".",h.headers[x])
        print("**********")
    
    def task5_4(self):
        # Modify the Header user-agent to display "Mobile" (task5.iv
        headers = {
            'User-Agent' : 'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10'
        }
        r2 = requests.get(url,headers=headers)
        print(r2.request.headers)


# Our scrapy code from https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3
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

# Task 8 : a Test Case with appropriate Test function(s) to test your application.
class Test(unittest.TestCase):
   bs=None
   def setUpClass():
      url="https://brickset.com/sets/year-2010"
      Test.bs=BeautifulSoup(urlopen(url), 'html.parser')
   def test_titleText(self):
      pageTitle=Test.bs.find('h1').get_text()
      self.assertEqual('Brickset', pageTitle); # ensure that the pagetitle have "Brickset"
   def test_contentExists(self):
      content=Test.bs.find('div',{'class':'content'}) # ensure the website have the correct div
      self.assertIsNotNone(content)

if __name__ == '__main__':
    unittest.main()

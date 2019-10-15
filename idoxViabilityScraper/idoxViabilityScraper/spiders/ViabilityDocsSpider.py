import scrapy
import csv
#import urllib.request
import wget


class ViabilityDocsSpider(scrapy.Spider):
    name = "viabilityDocs"

    def start_requests(self):
        url_header = "https://planning.southwark.gov.uk/online-applications/applicationDetails.do?activeTab=documents&keyVal="
        urls_all = []
        #with open('planningApps.csv', 'r') as csvfile:
        with open('docListing_all.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                    print(url_header, row[0], sep='')
                    urls_all.append(url_header + row[0])

        urls = urls_all
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("=")[-1]
        filename = 'docListingNew-%s.csv' % page
        #items = response.xpath("//*[@id='Documents']/tr[td//text()[contains(., 'VIABILITY')]]/td[7]/a/@href").getall()
        items = response.xpath("//*[@id='Documents']/tr[td//text()[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'viability')]]/td[7]/a/@href").getall() # using XPath 1.0 hack for matching case insensitive
        with open(filename, 'w') as f:
            for item in items:
                f.write("%s,%s,https://planning.southwark.gov.uk%s\n" % (page, response.url, item))
                url = "https://planning.southwark.gov.uk"+item
                print("URL: "+url)
                #urllib.request.urlretrieve(url, './')
                wget.download(url, '/Users/adamrae/Code/southwark-viability-scraper/idoxViabilityScraper/pdfs/')
            #f.write(response.body)
        self.log('Saved file %s' % filename)

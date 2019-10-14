import scrapy
import csv


class ViabilityDocsSpider(scrapy.Spider):
    name = "viabilityDocs"

    def start_requests(self):
        url_header = "https://planning.southwark.gov.uk/online-applications/applicationDetails.do?activeTab=documents&keyVal="
        urls_all = []
        with open('planningApps.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                    print(url_header, row[1], sep='')
                    urls_all.append(url_header + row[1])

        urls = urls_all
        #urls = [
        #    'https://planning.southwark.gov.uk/online-applications/applicationDetails.do?activeTab=documents&keyVal=ZZZV0PKBWR258',
        #    'https://planning.southwark.gov.uk/online-applications/applicationDetails.do?activeTab=documents&keyVal=ZZZV0NKBWR928',
        #    'https://planning.southwark.gov.uk/online-applications/applicationDetails.do?activeTab=documents&keyVal=ZZZV0NKBWR746'
        #]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("=")[-1]
        filename = 'docListing-%s.csv' % page
        #items = response.xpath("//*[@id='Documents']/tr[td//text()[contains(., 'VIABILITY')]]/td[7]/a/@href").getall()
        items = response.xpath("//*[@id='Documents']/tr[td//text()[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'viability')]]/td[7]/a/@href").getall() # using XPath 1.0 hack for matching case insensitive
        with open(filename, 'w') as f:
            for item in items:
                f.write("%s, %s, https://planning.southwark.gov.uk%s\n" % (page, response.url, item))
            #f.write(response.body)
        self.log('Saved file %s' % filename)

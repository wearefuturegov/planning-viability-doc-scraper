import scrapy
import csv
import wget
import sys

class ViabilityDocsSpiderTowerHamlets(scrapy.Spider):
	name = "viabilityDocsTowerHamlets"
	
	def start_requests(self):
		try:
			urlsFile = self.urlsFile
		except:
			print("ERROR: URL file argument not set!")
			sys.exit(1)
			
		try:
			outputPDFs = self.outputPDFs
		except:
			print("ERROR: Output PDF location not set!")
			sys.exit(1)
			
		try:
			outputCSVs = self.outputCSVs
		except:
			print("ERROR: Output CSV location not set!")
			sys.exit(1)
			
		url_header = "https://development.towerhamlets.gov.uk/online-applications/applicationDetails.do?activeTab=documents&keyVal=DCAPR_"
		urls_all = []
		with open(self.urlsFile, 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter=',', quotechar='"')
			for row in reader:
					urls_all.append(url_header + row[1])

		urls = urls_all
		for i, url in enumerate(urls):
			yield scrapy.Request(url=url, meta={'cookiejar': i}, callback=self.parseApplicationPage)


	def parseApplicationPage(self, response):
		page = response.url.split("=")[-1]
		filename = '/THdocListingNew-%s.csv' % page
		filename = self.outputCSVs + filename
		#print("FILENAME: ", filename)
		items = response.xpath("//*[@id='Documents']/tr[td//text()[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'viability')]]/td[6]/a/@href").getall() # using XPath 1.0 hack for matching case insensitive
		with open(filename, 'w') as f:
			#f.write(response.body)
			for item in items:
				f.write("%s,%s,https://development.towerhamlets.gov.uk%s\n" % (page, response.url, item))
				url = "https://development.towerhamlets.gov.uk"+item
				print("URL: "+url)
				yield scrapy.Request(url=url, meta={'cookiejar': response.meta['cookiejar']}, callback=self.retrieveViabilityDoc)
		self.log('Saved file %s' % filename)
		
	def retrieveViabilityDoc(self, response):
		page = response.url.split("/")[-1]
		filename = '/THdocListingNew-%s' % page
		filename = self.outputPDFs+filename
		print("INFO: Filename = %s" % filename)
		pdf = response.body
		with open(filename, 'wb') as f:
			f.write(pdf)
		self.log('LOG: Saved viability doc')

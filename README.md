# Planning Viability Appraisal Scraper

Purpose: Retrieve documents containing planning viability data associated with developments within a local authority. Currently only works for Southwark and Tower Hamlets.

![](https://github.com/wearefuturegov/planning-viability-doc-scraper/blob/master/documentation/process.png)

![](https://github.com/wearefuturegov/planning-viability-doc-scraper/blob/master/documentation/extension.png)

Note: Play nicely with other people's servers.

Contact: https://github.com/raemond

## Deploy Instructions
`virtualenv .env && source .env/bin/activate && pip install -r requirements.txt`

## Running the crawler
`scrapy crawl viabilityDocsSouthwark -s JOBDIR=crawls/somespider-1 -a urlsFile=docListing_all.csv -a outputPDFs=../idoxViabilityScraper/pdfs -a outputCSVs=../idoxViabilityScraper/csvs`

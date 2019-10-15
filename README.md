# Viability Appraisal Scraper

Project: Planning Viability

## Deploy Instructions
`virtualenv .env && source .env/bin/activate && pip install -r requirements.txt`

## Running the crawler
`scrapy crawl viabilityDocsSouthwark -a urlsFile=docListing_all.csv -a outputPDFs=../idoxViabilityScraper/pdfs -a outputCSVs=../idoxViabilityScraper/csvs`
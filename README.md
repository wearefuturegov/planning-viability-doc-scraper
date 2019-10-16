# Viability Appraisal Scraper

Project: Planning Viability

## Deploy Instructions
`virtualenv .env && source .env/bin/activate && pip install -r requirements.txt`

## Running the crawler
`scrapy crawl viabilityDocsSouthwark -s JOBDIR=crawls/somespider-1 -a urlsFile=docListing_all.csv -a outputPDFs=../idoxViabilityScraper/pdfs -a outputCSVs=../idoxViabilityScraper/csvs`

## TODO
- Add use of job dir to running instruction: [https://docs.scrapy.org/en/latest/topics/jobs.html](https://docs.scrapy.org/en/latest/topics/jobs.html)
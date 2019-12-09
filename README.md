# Planning Viability Appraisal Scraper

Purpose: Retrieve documents containing planning viability data associated with developments within a local authority. Currently only works for Southwark and Tower Hamlets, but should be easily extended to other local authorities using similar planning portals.

The expected data processing follows this chain:

![](https://github.com/wearefuturegov/planning-viability-doc-scraper/blob/master/documentation/process.png)

... and this scraper does Steps 2, 3 and 4.

The intention is ultimately to extract key values from the viability assessments. This will prioritise the values that Local Authorities have said are most important when establishing the context of an assessment. It would then be extended with further levels of detail that woud support greater scrutiny.

![](https://github.com/wearefuturegov/planning-viability-doc-scraper/blob/master/documentation/extension.png)

Note: Play nicely with other people's servers.

Contact: https://github.com/raemond

## Deploy Instructions
`virtualenv .env && source .env/bin/activate && pip install -r requirements.txt`

## Running the crawler
`scrapy crawl viabilityDocsSouthwark -s JOBDIR=crawls/somespider-1 -a urlsFile=docListing_all.csv -a outputPDFs=../idoxViabilityScraper/pdfs -a outputCSVs=../idoxViabilityScraper/csvs`

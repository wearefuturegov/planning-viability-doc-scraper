# Planning Viability Appraisal Scraper

## Description

This scrap retrieves documents containing planning viability data associated with developments within a given local authority. Currently only works for Southwark and Tower Hamlets, but should be extended to other local authorities using similar planning portals (iDox).

The expected data processing follows this chain:

![](https://github.com/wearefuturegov/planning-viability-doc-scraper/blob/master/documentation/process.png)

... and this scraper does Steps 2, 3 and 4. Step 1 is done by accesing the relevant planning auhtority's public facing GIS platform in a tool like QGIS and extracting the internal IDs for each development.

The intention for this tool is ultimately to extract key values from the viability assessments. This will prioritise the values that Local Authorities have said are most important when establishing the context of an assessment. It would then be extended with further levels of detail that woud support greater scrutiny.

![](https://github.com/wearefuturegov/planning-viability-doc-scraper/blob/master/documentation/extension.png)

For table extraction, tools like [Camelot](https://camelot-py.readthedocs.io/en/master/) or [Textract](https://aws.amazon.com/textract/) could be used.

## Usage Note 

Play nicely with other people's servers.

## Deploy Instructions
`virtualenv .env && source .env/bin/activate && pip install -r requirements.txt`

## Running the crawler
`scrapy crawl viabilityDocsSouthwark -s JOBDIR=crawls/somespider-1 -a urlsFile=docListing_all.csv -a outputPDFs=../idoxViabilityScraper/pdfs -a outputCSVs=../idoxViabilityScraper/csvs`

## Contact

[https://github.com/raemond](https://github.com/raemond)

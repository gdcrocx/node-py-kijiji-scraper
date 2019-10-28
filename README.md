# node-py-kijiji-scraper
This is a node-py package for scraping ads off Kijiji using Node.Js and Python to filter out custom keywords and remove duplicates.

Run the scripts in this order for results without error messages.

- NodeKijijiScraper.js - Fetch Kijiji Ads based on given filter criteria and returns a JSON file for Python parsing.
- kijijiWeeder.py - Remove ads from the JSON file that match exclusion criteria
- kijijiDeduplication.py - Remove duplicates from the JSON file based on matching or similar Ad attributes

# Credits

### NodeJs Library - 
@mwpenny - https://github.com/mwpenny/kijiji-scraper
 - A lightweight node.js module for retrieving and scraping ads from Kijiji using node, cheerio and node-fetch libraries.

Thank you @mwpenny for your contributions.
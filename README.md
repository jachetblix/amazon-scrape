# Amazon Review Scraper

This project is a Python web scraper that extracts product reviews from Amazon using BeautifulSoup and urllib. It's designed to work with a proxy to avoid IP blocking by Amazon.

## Prerequisites


Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- Required Python packages installed. You can install them using pip.

## Installation
```
git clone https://github.com/jachetblix/amazon-scrape.git
cd amazon-scrape
pip install -r requirements.txt
```

##  Run the scraper
```
python3 main.py PROXY_URL

```

The scraped reviews will be saved to a JSON file named amazon_reviews.json.


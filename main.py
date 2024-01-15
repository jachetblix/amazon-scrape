import urllib.request
import ssl
from bs4 import BeautifulSoup
import json

# Define your proxy configuration
proxy_url = ''  # for this project I used BrightData unblocker, you can use it here also

ssl._create_default_https_context = ssl._create_unverified_context

base_url = 'https://www.amazon.com/Samsung-27-inch-Business-C27F390FHN-LED-Lit/product-reviews/B01IPHVFUI/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&sortBy=recent&formatType=current_format'

proxy_handler = urllib.request.ProxyHandler({'http': proxy_url, 'https': proxy_url})

# Build an opener with the proxy handler
opener = urllib.request.build_opener(proxy_handler)


# Function to scrape reviews from a single page
def scrape_reviews(url):
    try:
        response = opener.open(url)
        html = response.read()
    except Exception as e:
        print("Error downloading HTML:", str(e))
        return []

    soup = BeautifulSoup(html, 'html.parser')

    # Extract and store the reviews
    reviews = []

    review_cards = soup.find_all('div', {'data-hook': 'review'})

    for review_card in review_cards:
        # Extract author name
        author_element = review_card.find('span', {'class': 'a-profile-name'})
        author = author_element.text.strip() if author_element else "Author not found"

        # Extract date
        date_element = review_card.find('span', {'data-hook': 'review-date'})
        date = date_element.text.strip() if date_element else "Date not found"

        # Extract rating
        rating_element = review_card.find('i', {'data-hook': 'review-star-rating'}).find('span', class_='a-icon-alt')
        rating = rating_element.text.strip() if rating_element else "Rating not found"

        # Extract review body
        review_body_element = review_card.find('span', {'data-hook': 'review-body'})
        review_body = review_body_element.text.strip() if review_body_element else "Review body not found"

        review_data = {
            'Author': author,
            'Date': date,
            'Rating': rating,
            'Review Body': review_body
        }

        # Append the review data to the list of reviews
        reviews.append(review_data)
    return reviews


# Function to scrape reviews from multiple pages
def scrape_all_reviews(base_url):
    all_reviews = []
    page = 1

    while True:
        page_url = f"{base_url}&pageNumber={page}"
        reviews = scrape_reviews(page_url)

        if not reviews:
            break

        all_reviews.extend(reviews)
        page += 1

    return all_reviews


# Scrape reviews from multiple pages
all_reviews = scrape_all_reviews(base_url)

# Save all the reviews as a JSON file
with open('amazon_reviews.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_reviews, json_file, indent=4, ensure_ascii=False)
print(f"Amazon product reviews from {base_url} pages have been scraped and saved to 'amazon_reviews.json'.")

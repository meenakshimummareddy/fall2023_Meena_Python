import requests
from bs4 import BeautifulSoup

# Define a list of websites to scrape
websites = ["https://example1.com", "https://example2.com"]

for url in websites:
    # Send a GET request
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract and print relevant information
    headlines = soup.find_all("h2")
    print(f"Headlines from {url}:")
    for headline in headlines:
        print(headline.text)

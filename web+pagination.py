import requests
from bs4 import BeautifulSoup

# Subheading 1: Define the URL and initialize variables
base_url = "https://example.com/page"
page_number = 1
results = []

# Subheading 2: Loop through multiple pages and scrape data
while True:
    url = f"{base_url}/{page_number}"
    response = requests.get(url)
    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("div", class_="result-item")

    # Subheading 3: Extract and process data
    for item in data:
        title = item.find("h2").text
        description = item.find("p").text
        results.append({"title": title, "description": description})

    page_number += 1

# Subheading 4: Analyze and display the scraped data
for result in results:
    print(f"Title: {result['title']}")
    print(f"Description: {result['description']}")

# -------------------------------------------------------------------------
# AUTHOR: Nikhitha Vasiraju
# FILENAME: scraper.py
# SPECIFICATION: Crawl the Circular Links section of TestingURL.dev.
# FOR: CS 4250 - Assignment #2
# TIME SPENT: 45 minutes
# -------------------------------------------------------------------------

# Importing Python libraries
from collections import deque
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

# Defining the seed URL
seed = "https://testingurl.dev/scraping/links/circular"
baseURL = "https://testingurl.dev"

# Creating the frontier and seen collections
frontier = deque([seed])
seen = {seed}


# Crawling until the frontier is empty
while frontier:

    # Removing the first URL from the frontier
    url = frontier.popleft()


    # Retrieving and parsing the Web page
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")


    # Printing the text contained in the <h1> element
    h1 = soup.find("h1")
    if h1 is not None:
        print(h1.get_text(strip=True))


    # Extracting and processing hyperlinks
    for anchor in soup.find_all("a", href=True):
        absoluteURL = urljoin(url, anchor["href"])

        if absoluteURL.startswith(seed) and absoluteURL not in seen:
            seen.add(absoluteURL)
            frontier.append(absoluteURL)


# Printing all URLs in seen
for url in seen:
    print(url)

import pandas as pd
import requests
from bs4 import BeautifulSoup

# Takes URL as input and returns time piece was published and piece's tags
def scrapeTags(url):
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    tags = []
    times = None

    # Scrapes time from URL
    time = soup.find('time')
    if time != None:
        times = pd.to_datetime(time.text)

    # Scrapes tags from URL
    for elem in soup.find_all('a', class_ = 'elementor-post-info__terms-list-item'):
        tags.append(elem.text.strip())
    
    return (times, tags)
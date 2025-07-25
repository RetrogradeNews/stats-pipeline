import pandas as pd
import requests
from bs4 import BeautifulSoup

# Top: Categories; Bottom: Tags
notNames = ['Life & Arts', 'Comics & Activities', 'History', 'Wild Art', 'News', 'Breaking News', 'News Brief', 'Student Government', 'Newspaper', 'Opinion', 'Editor’s Desk', 'Editorial', 'Letter to the Editor', 'Op-Ed', 'Sports', 'Basketball', 'Chess', 'Esports', 'Uncategorized', 
           'Featured', 'Breaking News', 'Construction', 'Highlight', 'Immigration', 'In Case You Missed It', 'UTD Esports']

def scraper(path):
    df = pd.read_csv(path, names=["title", "views", "url"])
    
    tags = []
    times = []

    for url in df["url"]:
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        tags.append([])
        time = soup.find('time')
        if time == None:
            times.append(None)
            continue
        times.append(pd.to_datetime(time.text))

        for elem in soup.find_all('a', class_ = 'elementor-post-info__terms-list-item'):
            tags[-1].append(elem.text.strip())

    df['times'] = times
    df["tags"] = tags

    df.to_csv("data\\data.csv", index=False)
import os

from scraping import scraper

csvLocation = 'data\\rg.csv'

def main():
    scrape = True
    if os.path.exists("data\\data.csv"):
        print("Do you want to re-scrape the data?")
        if input("(y/n): ").lower() == 'n':
            scrape = False
    
    if scrape:
        scraper(csvLocation)

    print("Done!")
        

if __name__ == "__main__":
    main()
import pandas as pd

# Cleans and selects data from pertinent timeframe
def clean(df):
    # Removes all non-piece pages
    newdf = df.dropna()

    # Specifies interval of time pipeline processes
    start_date = pd.Timestamp("2000-01-01")
    end_date = pd.Timestamp("2025-06-21")
    newdf = newdf[(newdf['times'] >= start_date) & (newdf['times'] <= end_date)]
    return newdf

# Finds category of piece from tags
def findCategory(tags):
    categories = ['News', 'Life & Arts', 'Opinion', 'Comics & Activities', 'Sports', 'Newspaper', 'History', 'Wild Art', 'Breaking News', 'News Brief', 'Student Government', "Editor's Desk", 'Editor’s Desk', 'Editorial', 'Letter to the Editor', 'Op-Ed', 'Basketball', 'Chess', 'Esports', 'Uncategorized']
    for category in categories:
        if category in tags:
            return category
    return None

# Reduces categories to their base components
def simplifyCategories(df):
    newdf = df
    newdf["category"] = newdf["category"].replace(['Breaking News', 'News Brief', 'Student Government'], "News")
    newdf["category"] = newdf["category"].replace(['Wild Art'], 'Life & Arts')
    newdf["category"] = newdf["category"].replace(["Editor's Desk", 'Editor’s Desk', 'Editorial', 'Letter to the Editor', 'Op-Ed'], 'Opinion')
    newdf["category"] = newdf["category"].replace(['Basketball', 'Chess', 'Esports'], 'Sports')
    return newdf

# Returns dataframe with pieces listed by author
def findAuthors(df):
    # Top: Categories; Bottom: Tags
    notNames = ['Life & Arts', 'Comics & Activities', 'History', 'Wild Art', 'News', 'Breaking News', 'News Brief', 'Student Government', 'Newspaper', 'Opinion', 'Editor’s Desk', "Editor's Desk", 'Editorial', 'Letter to the Editor', 'Op-Ed', 'Sports', 'Basketball', 'Chess', 'Esports', 'Uncategorized', 
        'Featured', 'Breaking News', 'Construction', 'Highlight', 'Immigration', 'In Case You Missed It', 'UTD Esports']

    newdf = df[~df["tags"].apply(lambda tags: 'Op-Ed' in tags)] # Filters out op-eds
    newdf = df.explode('tags') # Takes dataframe and creates new entry by tag
    newdf = newdf[~newdf['tags'].isin(notNames)] # Filters out tags that aren't names
    newdf = newdf[['tags'] + [col for col in newdf.columns if col != 'tags']] # Puts name column in front
    return newdf
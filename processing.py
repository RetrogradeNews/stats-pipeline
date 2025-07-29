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

# Returns dataframe with pieces listed by author
def findAuthors(df):
    # Top: Categories; Bottom: Tags
    notNames = ['Life & Arts', 'Comics & Activities', 'History', 'Wild Art', 'News', 'Breaking News', 'News Brief', 'Student Government', 'Newspaper', 'Opinion', 'Editor’s Desk', "Editor's Desk", 'Editorial', 'Letter to the Editor', 'Op-Ed', 'Sports', 'Basketball', 'Chess', 'Esports', 'Uncategorized', 
        'Featured', 'Breaking News', 'Construction', 'Highlight', 'Immigration', 'In Case You Missed It', 'UTD Esports']

    newdf = df.explode('tags') # Takes dataframe and creates new entry by tag
    newdf = newdf[~newdf['tags'].isin(notNames)] # Filters out tags that aren't names
    newdf = newdf[['tags'] + [col for col in newdf.columns if col != 'tags']] # Puts name column in front
    return newdf
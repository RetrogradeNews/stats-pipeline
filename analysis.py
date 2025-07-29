from graphics import createGraphic

# Analyzes data by author and creates graphics
def analyze(df):
    # Calculates stats for each author/artist
    authors = df["tags"].unique()
    for author in authors:
        authordf = df[df["tags"] == author]
        numPieces = len(authordf)
        mostViews = authordf.loc[authordf["views"].idxmax()]["title"]
        totalViews = authordf["views"].sum()
        
        # Calls graphics creation for data
        createGraphic(author, numPieces, mostViews, totalViews)



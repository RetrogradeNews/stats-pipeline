from graphics import createGraphic

def analyze(df):
    authors = df["tags"].unique()
    for author in authors:
        authordf = df[df["tags"] == author]
        numPieces = len(authordf)
        mostViews = authordf.loc[authordf["views"].idxmax()]["title"]
        totalViews = authordf["views"].sum()
        #createGraphic(author, numPieces, mostViews, totalViews)



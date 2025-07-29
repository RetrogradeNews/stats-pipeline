import os
import ast
import pandas as pd

from scraping import scrapeTags
from processing import findAuthors

def main():
  csvLocation = 'data\\rg.csv'
  dataLocation = "data\\data.csv"
  df = pd.read_csv(csvLocation, names=["title", "views", "url"])
  
  # Checks if data is alr processed or if user wants to reprocess data
  scrape = True
  if os.path.exists(dataLocation):
    print("Data detected. Do you want to re-scrape the data?")
    if input("(y/n): ").lower() == 'n':
      scrape = False

  # Rescrapes data and saves to file OR Loads dataframe from data file
  if scrape:
    df[['times', 'tags']] = df['url'].apply(lambda x: pd.Series(scrapeTags(x)))
    df.to_csv(dataLocation, index=False)
  else:
    df = pd.read_csv(dataLocation)
    df['tags'] = df['tags'].apply(ast.literal_eval)

  # Removes all non-piece pages
  df = df.dropna()

  # Finds piece by author
  dfAuthors = findAuthors(df)
  print(dfAuthors)
  
  print("Done!")
        

# Swag-based print statements
def swag():
    print("""                             ..                                
                    ...                 .                      
                .                            .                 
             .                                  .              
           .                                       .           
         .                                          ..         
                                                      .        
      .                                                        
                    #%%%%%%%%##%%%#-                     .     
   .                   .%%%       -%%%.                   .    
                        %%%        :%%%+++++++++-.         .   
                        %%%    ..++=%%%.       :+++.           
                        %%% .++.    %%%           ++           
                        %%%.       .%%.            +.          
                      .+%%%        %*              =           
                    =:  %%%*==+*%%.               .:          .
                  =.    %%%    .%%%.             .:            
                =       %%%      #%%+           .:            .
              .:        %%%       -%%%.        =               
             -          %%%        .%%%:     :.               .
            +           %%%          *%%%. :.                  
           +=           %%%           .%%*#                  . 
 .         +-          .%%%           .-=%%%%.                 
  .       :++       **+=====+*+    -=.    -******              
           +++.               .=+.                             
            +++++=--:--=+++++.                            .    
     .        .-=++++=-:                                       
      .                                                        
                                                      .        
                                                               
           .                                                   
              .                                 .              
                 .                                             
                      .                 .                      
    """)
    print("\"THE RETROGRADE\"")
    print("PIPELINE BY MUAAZ ABED\n")

if __name__ == "__main__":
  swag()
  main()
import os
import pandas as pd

from scraping import scrapeTags

csvLocation = 'data\\rg.csv'

def main():
    df = pd.read_csv(csvLocation, names=["title", "views", "url"])
    
    # Checks if data is alr processed or if user wants to reprocess data
    scrape = True
    if os.path.exists("data\\data.csv"):
      print("Data detected. Do you want to re-scrape the data?")
      if input("(y/n): ").lower() == 'n':
          scrape = False

    # Rescrapes data OR Loads from data file
    if scrape:
      df[['times', 'tags']] = df['url'].apply(lambda x: pd.Series(scrapeTags(x)))
      df.to_csv("data\\data.csv", index=False)
    else:
      df = pd.read_csv("data\\data.csv", names=["title", "views", "url", "times", "tags"])

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
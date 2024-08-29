from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt
import textwrap

#SetUpChromeDriver - Downloads and sets up the correct chrome driver for the designated computer
#   return: returns the newly created driver
def SetUpChromeDriver():
    # Download the correct ChromeDriver
    chromeDriver = ChromeDriverManager().install()

    # Create an options for specifications on how to run the driver
    chromeOptions = Options()

    # Add an option for Chrome to run in the background instead of opening a physical window
    chromeOptions.add_argument("--headless=new")

    # return Chrome
    return webdriver.Chrome(service=Service(chromeDriver), options=chromeOptions)

#createDF - Performs webscraping on www.allmusic.com and creates a dataframe of newly released albums
#   return - the dataframe modified to only include albums that have a rating
def createDF(driver):
    #link format for dates yy-month-day
    date = "20240823"
    url = "https://www.allmusic.com/newreleases/all/" + date

    #list representing the columns
    artists_list = []
    album_names_list = []
    labels_list = []
    genres_list = []
    ratings_list = []

    # Open the website to be scraped 
    driver.get(url)

    #Get all the artists in the page
    artists = driver.find_elements(By.XPATH, "//td[@class='artist']")
    albums = driver.find_elements(By.XPATH, "//td[@class='album']")
    labels = driver.find_elements(By.XPATH, "//td[@class='label']")
    genres = driver.find_elements(By.XPATH, "//td[@class='genre']")
    ratings = driver.find_elements(By.XPATH, "//td[@class='rating']")

    #one loop since all lists have the same length. TODO: Do we need to split?
    for entry in range(len(artists)):
        artists_list.append(artists[entry].text)
        album_names_list.append(albums[entry].text)
        labels_list.append(labels[entry].text)
        genres_list.append(genres[entry].text)
        ratings_list.append(ratings[entry].text)

    data_tuples = list(zip(artists_list[1:], album_names_list[1:], labels_list[1:], genres_list[1:], ratings_list[1:]))

    #create base dataframe
    df = pd.DataFrame(data_tuples, columns=['Artist','Album', 'Label', 'Genre', 'Rating'])

    #return the cleaned dataframe
    return df

#createAndShowPlot - creates and shows a bar graph comparing the top 5 genres with the most album releases. The x-axis being the genre and y-axis number of albums released  
def createAndShowPlot(df):
    #get the top 5 most common genres
    top_genres = df['Genre'].value_counts().nlargest(5)

    #create the bar plot
    top_genres.plot(kind='bar')

    #set a label for the x and y axes and a title
    plt.xlabel("Genre", labelpad=20)
    plt.ylabel("# of Albums", labelpad=20)
    plt.title("Album Releases By Genre August 2024")

    #get the current axis
    ax = plt.gca()

    #make the x-axis labels horizontal for easier readability and apply a textwrap so labels don't overlap
    ax.set_xticklabels([textwrap.fill(label, 15) for label in top_genres.index], rotation=0)

    # Adjust layout to prevent clipping
    plt.tight_layout()

    #show the plot
    plt.show()

def main():
    # get and start chrome driver
    driver = SetUpChromeDriver()

    # scrape the website and create the dataframe
    df = createDF(driver)

    # quit Chrome since we are done scraping
    driver.quit()
    
    # create and show the plot
    createAndShowPlot(df)

#ensure main is only run when the script is executed directly
if __name__ == "__main__":
    main()
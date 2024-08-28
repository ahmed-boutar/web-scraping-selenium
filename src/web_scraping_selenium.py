from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

# Download the correct ChromeDriver
chromeDriver = ChromeDriverManager().install()

# Create an options for specifications on how to run the driver
chromeOptions = Options()

# Add an option for Chrome to run in the background instead of opening a physical window
chromeOptions.add_argument("--headless=new")

# Start Chrome
driver = webdriver.Chrome(service=Service(chromeDriver), options=chromeOptions)

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
temp_df = pd.DataFrame(data_tuples, columns=['Artist','Album', 'Label', 'Genre', 'Rating'])

    

    
# Shut the driver down
driver.quit()
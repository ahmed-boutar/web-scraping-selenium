from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Download the correct ChromeDriver
chromeDriver = ChromeDriverManager().install()

# Start Chrome
driver = webdriver.Chrome(service=Service(chromeDriver))

# Open the website to be scraped 
driver.get('https://hoopshype.com/salaries/players/')
    
# Shut the driver down
driver.close()
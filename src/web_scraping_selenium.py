from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Download the correct ChromeDriver
chromeDriver = ChromeDriverManager().install()

# Create an options for specifications on how to run the driver
chromeOptions = Options()

# Add an option for Chrome to run in the background instead of opening a physical window
chromeOptions.add_argument("--headless=new")

# Start Chrome
driver = webdriver.Chrome(service=Service(chromeDriver), options=chromeOptions)
    
# Shut the driver down
driver.quit()
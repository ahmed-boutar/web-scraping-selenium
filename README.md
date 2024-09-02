## Team Name: Deftones  
#### Team Members: Tal Erez, Ahmed Boutar 
#### Topic: Web Scraping With Selenium

## Submission Description:
The script file is used to scrape the new releases included in the link https://www.allmusic.com/newreleases/all/
Specifically, we are scraping these urls, which represent all the albums released in the month of August 2024. Note: releases happen from every Friday. In our current context, the first Friday is on August 02, 2024: 

https://www.allmusic.com/newreleases/all/20240830 https://www.allmusic.com/newreleases/all/20240823
https://www.allmusic.com/newreleases/all/20240816
https://www.allmusic.com/newreleases/all/20240809
https://www.allmusic.com/newreleases/all/20240802

## List of Python scripts included in the submission:  
web_scraping_selenium.py

___Note:___ Since the rubric asked for specifically one .py script and not other files, we are including our requirements here: 
## Required Dependencies:
numpy==1.24.3 <br>
pandas==2.0.3 <br>
matplotlib==3.7.1 <br>
selenium==4.10.0 <br>
webdriver_manager==4.0.2 <br>
openpyxl==3.1.5 <br>


## Additional requirements: 
- Ensure that you are running Python3.11
- Ensure that you have Excel or an ExcelViewer on your computer

## Instructions to run:
### 1. Change the directory to where the web_scraping_selenium.py is 
### 2. Create a requirements.txt 
### 3. Paste the dependencies included above in the requirements.txt file
### 4. Set-up and activate the virtual environment:
Mac OS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```
Windows:
```
python -m venv venv
venv\Scripts\activate
```
### 5. Install the required dependencies
```
pip install -r requirements.txt
```
### 6. Run the script
```
python web_scraping_selenium.py
```

## Script Description
### Data used:
This script uses selenium to scrape the website www.allmusic.com containing information about new releases. It collects the information about the albums released in August 2024 and runs analysis on the data. 

### Functionality:
The script uses the selenium library to scrape the allmusic website and collect the new releases in August 2024. We used the Select function in selenium to select the albums that were “just released” and avoid collecting the albums that were re-issued, since we didn’t think they were relevant to our goal of analyzing new albums. However, we couldn’t exclude the albums that were re-mastered or re-released by a different labels as we didn’t find a separate datasets to check for that information. Some of the albums we collected did not have a record label associated with them. We figured that they were either released independently or through a record label that is not famous (yet). Since we didn’t find another recent dataset that would allow us to see which albums were released independently and which ones were released with a label that is not very known, we chose to use “Other” as the record label to represent this. 

### Results:
1. The script plots the data to see the number of new albums released in August 2024 by genre and the number of new albums released in August by record labels (picked the top 10) 
2. The script creates a list of the top 20 albums of August according to all music’s rating. To do that, we dropped all albums that had no rating associated with them. It saves the top 20 albums in an excel sheet. 

### Notes:
All functions contain a docstring outlining what the function does, its input parameters (if any) and output (if any). Comments are included above relevant lines of code to explain what they do and why they are used (depending on what they are used for. We tried to follow the best practices in writing code according to Pep 8 - Style Guide for Python Code (Reference: https://peps.python.org/pep-0008/) 

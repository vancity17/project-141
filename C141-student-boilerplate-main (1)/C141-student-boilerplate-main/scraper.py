from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## ADD CODE HERE ##
        soup = BeautifulSoup(browser.page_source,"html.parser")

        for ul_tag in soup.find_all("ul",attrs={"class,"exoplanet}):
         li_tags = ul_tag.find_all("li")
         temp_list = []
         for index, li_tag in enumerate(li_tags):
            if index == 0:
               temp_list.append(li_tag.find_all("a")[0].contents[0])
                    



        
# Calling Method    
scrape()

# Define Header
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Define pandas DataFrame   


# Convert to CSV

    



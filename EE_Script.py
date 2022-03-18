from urllib.request import urlopen
import pandas as panda

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

import matplotlib.pyplot as plot

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#RE-RUN IF U GET THIS ERROR - selenium.common.exceptions.WebDriverException: Message: target frame detached
#Todo: debug and fix later.

#Need to store this as an environmental variable
PATH = Service("/Users/amiteshnagarkar/Python/SA-Skills-Test/driver/chromedriver")


#Global
show_all_xpath = "/html/body/div[2]/div[3]/div/div/div/article/div/div[4]/button"
driver = webdriver.Chrome(service=PATH)

def GoToEe():

    eeWebsite = "https://shop.ee.co.uk/sim-only"
    accept_cookies = "/html/body/div[8]/div[1]/div/div[3]/a[1]"

    driver.get(eeWebsite)
    driver.implicitly_wait(10)
    
    
    #link.click()

    #WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, accept_cookies)))
    #wait = WebDriverWait(driver, 10)


    #WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, accept_cookies)))

    #driver.implicitly_wait(10)
   


    #iframe = driver.find_element(By.XPATH, "/html/body/iframe[3]")
    #driver.switch_to.frame(iframe)

    driver.find_element(By.CLASS_NAME, "mainContent")

    driver.implicitly_wait(10)

    link = driver.find_element(By.XPATH, accept_cookies)

    driver.execute_script("arguments[0].click();", link)
    driver.implicitly_wait(5)
    print("accepted cookies")

    
    #driver.switch_to.default_content()



#MAIN FUNCTION
def SimOnlyScraperMain():
    print ("Web Scraper in progress, please wait...")
    GoToEe()
    print ("We are scraping from the O2 Website...")
    print("INFO: If you get the below error, please re-run the script.")
    print("selenium.common.exceptions.WebDriverException: Message: target frame detached")
    #SimOnlyDealCollector()
    print ("Creating CSV file")
    #CreateCsv()
    print ("Creating a beautiful graph.")
    #MakeGraph()
    print("Sorry for the wait, all done now :)")
    driver.quit()

if __name__ == "__main__":
    SimOnlyScraperMain()
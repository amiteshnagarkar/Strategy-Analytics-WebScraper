from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = Service("/Users/amiteshnagarkar/Python/SA-Skills-Test/driver/chromedriver")

#block images and javascript requests to speed things up.
chrome_prefs = {
    "profile.default_content_setting_values": {
        "images": 2,
        "javascript": 2,
    }
}


def iPhoneScraper():
    print ("Scraping O2 for iphones...")
    o2_website = "https://www.o2.co.uk/iphone"
    see_all_xpath = "/html/body/section/div/div/section[5]/div/div/div[6]/div/div/section/div/div[2]/div/div/div/div/div/div/a/span[1]"
    show_all_xpath = "/html/body/div[2]/div[3]/div/div/div/article/div/div[4]/button"
    accept_cookies = "/html/body/div[6]/div/div/div[2]/button[1]"

    #xPATHS for iPhones:
    iPhone_13 = '/html/body/div[2]/div[3]/div/div/div/article/div/div[3]/div/div[1]/div/div/a/div[2]/div/div[1]'
    iPhone_SE_3rd_Gen = '/html/body/div[2]/div[3]/div/div/div/article/div/div[3]/div/div[5]/div/div/a/div[2]/div/div[1]/div'
    iPhone_13_Pro = '/html/body/div[2]/div[3]/div/div/div/article/div/div[3]/div/div[10]/div/div/a/div[2]/div/div[1]/div'
    iPhone_13_Pro_Max = '/html/body/div[2]/div[3]/div/div/div/article/div/div[3]/div/div[13]/div/div/a/div[2]/div/div[1]/div'
    iPhone_12_5G = '/html/body/div[2]/div[3]/div/div/div/article/div/div[3]/div/div[20]/div/div/a/div[2]/div/div[1]/div'
    iPhone_11 = '/html/body/div[2]/div[3]/div/div/div/article/div/div[3]/div/div[23]/div/div/a/div[2]/div/div[1]/div'
    xpath_list = [iPhone_13, iPhone_SE_3rd_Gen, iPhone_13_Pro, iPhone_13_Pro_Max, iPhone_12_5G, iPhone_11]

    #goes to o2 home site of Iphone
    driver = webdriver.Chrome(service=PATH)
    driver.implicitly_wait(5)
    driver.get(o2_website)
    driver.implicitly_wait(5)
    link = driver.find_element(By.XPATH, accept_cookies)
    link.click()
    driver.implicitly_wait(5)

    #goes to see all page
    link = driver.find_element(By.XPATH, see_all_xpath)
    link.click()
    driver.implicitly_wait(5)

    #goes to show all page
    link = driver.find_element(By.XPATH, show_all_xpath)
    link.click()
    driver.implicitly_wait(3)
   
    #this loop should collect all info needed for iPhones
    for phones in range(len(xpath_list)):

        driver.implicitly_wait(3)
        #loop this for different phones
        link = driver.find_element(By.XPATH, xpath_list[phones])
        link.click()

        #go to checkout with this specific phone

        #OR

        #grab all data from this specifc phone index page and store it somewhere, also take screenshot here





        



        driver.back()
        driver.implicitly_wait(3)

        driver.implicitly_wait(3)
        #goes to see all page again
        link = driver.find_element(By.XPATH, show_all_xpath)
        link.click()
        driver.implicitly_wait(3)

    
    driver.quit();


    










if __name__ == "__main__":
    iPhoneScraper();
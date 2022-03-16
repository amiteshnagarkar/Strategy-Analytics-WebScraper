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

import time

import pandas as pd

#RE-RUN IF U GET THIS - selenium.common.exceptions.WebDriverException: Message: target frame detached

PATH = Service("/Users/amiteshnagarkar/Python/SA-Skills-Test/driver/chromedriver")

#block images and javascript requests to speed things up.
chrome_prefs = {
    "profile.default_content_setting_values": {
        "images": 2,
        "javascript": 2,
    }
}

#change these to css selectors as they work best
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
    phone_name_list = []
    for phones in range(len(xpath_list)):

        driver.implicitly_wait(3)
        #loop this for different phones
        link = driver.find_element(By.XPATH, xpath_list[phones])
        link.click()
        driver.implicitly_wait(3)
        #go to all drop down if possible?

        #click choose this plan with this specific phone
        link = driver.find_element(By.CSS_SELECTOR, 'button.tne-secondary')
        link.click()
        driver.implicitly_wait(5)

        driver.maximize_window() # For maximizing window
        


        #choose later
        #driver.execute_script("window.scrollTo(0, 1000);")
        link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button')
        #driver.execute_script("window.scrollTo(0, window.scrollY + 1000)")

        driver.execute_script("scrollBy(0,-500);")
        time.sleep(2)

        driver.execute_script("scrollBy(0,400);")
        time.sleep(2)



        #driver.execute_script("arguments[0].scrollIntoView();",link)
        #link.click()
        driver.execute_script("arguments[0].click();", link)
        driver.implicitly_wait(5)

        #Confirm spend cap
        link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/div/div[6]/div/div/div/button/span')
        driver.execute_script("arguments[0].scrollIntoView();",link)
        #link.click()
        driver.execute_script("arguments[0].click();", link)
        driver.implicitly_wait(6)

        #No extras
        link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[2]/div/div[5]/div/div[2]/div/div/div[2]/div/div/div[1]/div[5]/div/div[2]')
        driver.implicitly_wait(5)
        driver.execute_script("arguments[0].scrollIntoView();",link)
        driver.implicitly_wait(5)
        #link.click()
        driver.execute_script("arguments[0].click();", link)
        driver.implicitly_wait(5)

        #No accessories
        link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[2]/div/div[5]/div/div[2]/div/div/div[2]/div/div/div[1]/div[5]/div/div[2]/button/div[1]')
        driver.execute_script("arguments[0].scrollIntoView();",link)
        #link.click()
        driver.execute_script("arguments[0].click();", link)
        driver.implicitly_wait(5)

        print("not gone to basket yet")
        #go to basket
        link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[2]/div/div[8]/div[2]/div/div/div/div/button/span')
        driver.execute_script("arguments[0].scrollIntoView();",link)
        #link.click()
        driver.execute_script("arguments[0].click();", link)
        driver.implicitly_wait(5)

        print("going to basket")


        

        #grab data
        phone_name = driver.find_element(By.CSS_SELECTOR, 'div.card-title').text
        driver.implicitly_wait(2)
        phone_model_and_month_plan = driver.find_element(By.CSS_SELECTOR, 'div.card-sentence').text
        driver.implicitly_wait(2)
        phone_upfront_cost = driver.find_element(By.CSS_SELECTOR, 'div.upfront-cost.ng-binding.ng-isolate-scope').text
        driver.implicitly_wait(2)
        phone_monthly_cost = driver.find_element(By.CSS_SELECTOR, 'div.upfront-cost.ng-binding.ng-isolate-scope').text
        driver.implicitly_wait(2)
        phone_tariff = driver.find_element(By.CSS_SELECTOR, 'div.card-sentence').text
        driver.implicitly_wait(2)
        phone_first_offer = driver.find_element(By.CSS_SELECTOR, 'p.offer-description.offer-text.activate-overlay.dynamic-overlay').text

        #add to list
        phone_name_list.append([phone_name, phone_model_and_month_plan, phone_upfront_cost, phone_monthly_cost, phone_tariff, phone_first_offer])

        #driver.implicitly_wait(3)

        #take screenshot
        driver.save_screenshot(('images/O2_iP_Screens/images/%s.png') %(xpath_list[phones]))

    
        driver.implicitly_wait(3)
        driver.back()
        driver.implicitly_wait(3)
        #OR

        #grab all data from this specifc phone index page and store it somewhere, also take screenshot here
        driver.back()
        

        driver.implicitly_wait(3)
        driver.back()
        driver.implicitly_wait(3)
        driver.back()
        driver.implicitly_wait(3)
        #goes to see all page again
        link = driver.find_element(By.XPATH, show_all_xpath)
        link.click()
        driver.implicitly_wait(3)

    print (phone_name_list)
    driver.quit()

    df = pd.DataFrame(phone_name_list, columns=["Phone Name", "Model & Month", "Upfront Cost", "Monthly Cost", "Phone Tariff", "1'st Offer"])
    df.to_csv('O2_iPhones.csv', index=False)
    










if __name__ == "__main__":
    iPhoneScraper();
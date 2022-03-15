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

#Having trouble locating xpath etc for ee cookie button?

#Only o2 and iPhone for Now.

#gets iPhone Data
def scrapePayMonthlyPhoneData():
  print('Scraping Phone Data..hold on...');
  nowTime = datetime.now()
  date_time_string = nowTime.strftime("%d/%m/%Y %H:%M:%S")
  pay_monthly_name = []
  pay_monthly_plan_length = []
  #automate these url collection
  IphoneSE5G_url1 = f"https://shop.ee.co.uk/mobile-phones/pay-monthly/iphone-se-5g/details"
  response = requests.get(IphoneSE5G_url1)
  htmlContent = response.content
  soup = BeautifulSoup(htmlContent, "html.parser")

  #device name
  for h1Tag in soup.find_all("h1", class_="h3 font-rubrik text-truncate-lines-5 text-left-md text-center"):
        pay_monthly_name.append(h1Tag.get_text(strip=True))
        bracket_removed_device_name=(','.join(pay_monthly_name))
        #return pay_monthly_name;

  #plan length
  for pTag in soup.find_all("p", class_="margin-bottom-3 colour-slate"):
        pay_monthly_plan_length.append(pTag.get_text(strip=True))
        bracket_removed_plan_length_name=(','.join(pay_monthly_plan_length))
        s = [float(s) for s in re.findall(r'-?\d+\.?\d*', bracket_removed_plan_length_name)]

        print("Date and Time: ",date_time_string);
        print("Device Name: ",bracket_removed_device_name);
        print(s);

def urlscraper():
    print ("Scraping o2 for Iphones...");
    url_list = []
    o2_website = "https://www.o2.co.uk/iphone"
    see_all_xpath = "/html/body/section/div/div/section[5]/div/div/div[6]/div/div/section/div/div[2]/div/div/div/div/div/div/a/span[1]"
    show_all_xpath = "/html/body/div[2]/div[3]/div/div/div/article/div/div[4]/button"
    accept_cookies = "/html/body/div[6]/div/div/div[2]/button[1]"

    #Xpaths for IPhones:
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
    #link = driver.find_element(By.TAG_NAME, "a")
    link.click()
    driver.implicitly_wait(5)

    #goes to show all page
    link = driver.find_element(By.XPATH, show_all_xpath)
    #link = driver.find_element(By.TAG_NAME, "a")
    link.click()
    driver.implicitly_wait(5)



    
    for phones in range(len(xpath_list)):

        #loop this for different phones
        link = driver.find_element(By.XPATH, xpath_list[phones])
        link.click()
        url_list.append(driver.current_url)
        #print (url_list)

        # goes back to home page again
        driver.get(o2_website)
        link = driver.find_element(By.XPATH, see_all_xpath)
        link.click()

        #goes to see all page again
        link = driver.find_element(By.XPATH, show_all_xpath)
        link.click()
        driver.implicitly_wait(5)

    pass

    print (url_list)


if __name__ == "__main__":
    urlscraper();
    #scrapePayMonthlyPhoneData();
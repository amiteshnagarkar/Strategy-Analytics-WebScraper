from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

PATH = Service("/Users/amiteshnagarkar/Python/SA-Skills-Test/driver/chromedriver")


#Only EE and iPhone for Now.

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
    print ("hello");
    driver = webdriver.Chrome(service=PATH)
    driver.get("https://shop.ee.co.uk/gallery/pay-monthly/mobile-phones-h00001?search=%3AofferingsOrder%3AproductBrands%3Abrands_apple")


if __name__ == "__main__":
    urlscraper();
    #scrapePayMonthlyPhoneData();
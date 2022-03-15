from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date
from datetime import datetime

#Only EE for now.

def scrapePayMonthlyPhoneData():
  print('Scraping Phone Data..hold on...');

  nowTime = datetime.now()
  date_time_string = nowTime.strftime("%d/%m/%Y %H:%M:%S")
  pay_monthly_name = []
  pay_monthly_plan_length = []

  #automate these url collection
  IphoneSE5G_url1 = f"https://shop.ee.co.uk/mobile-phones/pay-monthly/iphone-se-5g/details"
  #SamsungGs22_url2 = f"https://shop.ee.co.uk/mobile-phones/pay-monthly/samsung-galaxy-s22-ultra-5g/details"
  #SamsungGs22Plus_url2 = f"https://shop.ee.co.uk/mobile-phones/pay-monthly/samsung-galaxy-s22-plus-5g/details?color=PinkGold&capacity=128GB"

  response = requests.get(IphoneSE5G_url1)
  htmlContent = response.content
  soup = BeautifulSoup(htmlContent, "html.parser")

  for h1Tag in soup.find_all("h1", class_="h3 font-rubrik text-truncate-lines-5 text-left-md text-center"):
        pay_monthly_name.append(h1Tag.get_text(strip=True))
        bracket_removed_device_name=(','.join(pay_monthly_name))
        #return pay_monthly_name;

  for pTag in soup.find_all("p", class_="margin-bottom-3 colour-slate"):
        pay_monthly_plan_length.append(pTag.get_text(strip=True))
        bracket_removed_plan_length_name=(','.join(pay_monthly_plan_length))
        s = [float(s) for s in re.findall(r'-?\d+\.?\d*', bracket_removed_plan_length_name)]

        print("Date and Time: ",date_time_string);
        print("Device Name: ",bracket_removed_device_name);
        print(s);


if __name__ == "__main__":
  scrapePayMonthlyPhoneData();

'''
Amitesh Nagarkar

Description: Scrapes data from O2 site.

'''

from urllib.request import urlopen
import pandas as panda

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

import matplotlib.pyplot as plot

PATH = Service("./driver/chromedriver")

#Global
show_all_xpath = "/html/body/div[2]/div[3]/div/div/div/article/div/div[4]/button"
driver = webdriver.Chrome(service=PATH)
phone_name_list = []

#Graph Maker    
def make_graph():
    dataFrame = panda.read_csv('O2_iPhones.csv')
    ax = dataFrame.set_index('Phone_Name').plot()
    ax.set_xlabel('iPhone Name', fontsize=10)
    ax.set_ylabel('Monthly Cost (£)', fontsize=10)
    ax.set_title('O2 - iPhone Pay Monthly Comparison', fontsize=18)
    plot.xticks(fontsize=3)
    plot.autoscale(enable=True, axis='both', tight=None)
    plot.savefig('O2_iPhones_Graph.png', dpi=200)

#Invoke browser, got to o2 site and list all iphones
def go_to_o2():
    print("Opening the browser and loading O2.")
    o2_website = "https://www.o2.co.uk/iphone"
    see_all_xpath = "/html/body/section/div/div/section[5]/div/div/div[6]/div/div/section/div/div[2]/div/div/div/div/div/div/a/span[1]"
    accept_cookies = "/html/body/div[6]/div/div/div[2]/button[1]"

    driver.implicitly_wait(5)
    driver.get(o2_website)
    driver.implicitly_wait(5)
    link = driver.find_element(By.XPATH, accept_cookies)
    link.click()
    driver.implicitly_wait(5)

    #See All iphones
    link = driver.find_element(By.XPATH, see_all_xpath)
    link.click()
    driver.implicitly_wait(5)

    #Show All iphones
    link = driver.find_element(By.XPATH, show_all_xpath)
    link.click()
    driver.implicitly_wait(3)

def create_csv():
    #Create CSV
    dataFrame = panda.DataFrame(phone_name_list, columns=["Phone_Name", "Model_Month", "Upfront_Cost", "Monthly_Cost", "Phone_Tariff", "First_Offer"])
    dataFrame.to_csv('O2_iPhones.csv', index=False)

def iphone_data_collector():
    #xPATHS for iPhones:
    iPhone_13 = '/html/body/div[2]/div[3]/div/div/div/article/div/div[3]/div/div[1]/div/div/a/div[2]/div/div[1]'
    iPhone_SE_3rd_Gen = '/html/body/div[2]/div[3]/div/div/div/article/div/div[3]/div/div[5]/div/div/a/div[2]/div/div[1]/div'
    iPhone_13_Pro = '/html/body/div[2]/div[3]/div/div/div/article/div/div[3]/div/div[10]/div/div/a/div[2]/div/div[1]/div'
    iPhone_13_Pro_Max = '/html/body/div[2]/div[3]/div/div/div/article/div/div[3]/div/div[13]/div/div/a/div[2]/div/div[1]/div'
    iPhone_12_5G = '/html/body/div[2]/div[3]/div/div/div/article/div/div[3]/div/div[20]/div/div/a/div[2]/div/div[1]/div'
    iPhone_11 = '/html/body/div[2]/div[3]/div/div/div/article/div/div[3]/div/div[23]/div/div/a/div[2]/div/div[1]/div'
    xpath_list = [iPhone_13, iPhone_SE_3rd_Gen, iPhone_13_Pro, iPhone_13_Pro_Max, iPhone_12_5G, iPhone_11]

    print("Now getting phone data from O2 site.")
    image_counter = 0;
    for phones in range(len(xpath_list)):

        driver.implicitly_wait(3)
        link = driver.find_element(By.XPATH, xpath_list[phones])
        link.click()
        driver.implicitly_wait(3)

        #Choose this plan
        link = driver.find_element(By.CSS_SELECTOR, 'button.tne-secondary')
        link.click()
        driver.implicitly_wait(5)
        driver.maximize_window() # For maximizing window
        
        #Choose Later
        link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button')
        driver.execute_script("scrollBy(0,-500);")
        time.sleep(2)
        driver.execute_script("scrollBy(0,400);")
        time.sleep(2)

        driver.execute_script("arguments[0].click();", link)
        driver.implicitly_wait(5)

        #Confirm Spend Cap, no spend cap chosen by default.
        link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/div/div[6]/div/div/div/button/span')
        driver.execute_script("arguments[0].scrollIntoView();",link)
        driver.execute_script("arguments[0].click();", link)
        driver.implicitly_wait(6)

        #No Extras
        link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[2]/div/div[5]/div/div[2]/div/div/div[2]/div/div/div[1]/div[5]/div/div[2]')
        driver.implicitly_wait(5)
        driver.execute_script("arguments[0].scrollIntoView();",link)
        driver.implicitly_wait(5)
        driver.execute_script("arguments[0].click();", link)
        driver.implicitly_wait(5)

        #No Accessories
        link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[2]/div/div[5]/div/div[2]/div/div/div[2]/div/div/div[1]/div[5]/div/div[2]/button/div[1]')
        driver.execute_script("arguments[0].scrollIntoView();",link)
        driver.execute_script("arguments[0].click();", link)
        driver.implicitly_wait(5)

        #Basket
        link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[2]/div/div[8]/div[2]/div/div/div/div/button/span')
        driver.execute_script("arguments[0].scrollIntoView();",link)
        driver.execute_script("arguments[0].click();", link)
        driver.implicitly_wait(5)

        #Get Specific Information from Phone
        phone_name = driver.find_element(By.CSS_SELECTOR, 'div.card-title').text
        driver.implicitly_wait(2)
        phone_model_and_month_plan = driver.find_element(By.CSS_SELECTOR, 'div.card-sentence').text
        driver.implicitly_wait(2)
        phone_upfront_cost = driver.find_element(By.CSS_SELECTOR, 'div.upfront-cost.ng-binding.ng-isolate-scope').text
        phone_upfront_cost = phone_upfront_cost.lstrip('£');
        driver.implicitly_wait(2)
        phone_monthly_cost = driver.find_element(By.CSS_SELECTOR ,'div#month-total.upfront-cost.total-upfront-cost.ng-binding.ng-isolate-scope').text
        phone_monthly_cost = phone_monthly_cost.lstrip('£');
        driver.implicitly_wait(2)
        phone_tariff = driver.find_element(By.CSS_SELECTOR, 'div.card-sentence').text
        driver.implicitly_wait(2)
        phone_first_offer = driver.find_element(By.CSS_SELECTOR, 'p.offer-description.offer-text.activate-overlay.dynamic-overlay').text

        #Add Collected Information to List
        phone_name_list.append([phone_name, phone_model_and_month_plan, phone_upfront_cost, phone_monthly_cost, phone_tariff, phone_first_offer])

        #Screenshot
        image_filename = 'images/O2_iP_Screens/images/screenshot_' + str(phone_name) + '_' + str(image_counter) + '.png'
        #Scroll works well to screenshot section.
        driver.execute_script("scrollBy(0,-500);")
        time.sleep(2)
        driver.execute_script("scrollBy(0,400);")
        driver.save_screenshot(image_filename);
        image_counter += 1;

        #See All iPhone Section again
        driver.implicitly_wait(3)
        driver.back()
        driver.implicitly_wait(3)
        driver.back()
        driver.implicitly_wait(3)
        driver.back()
        driver.implicitly_wait(3)
        driver.back()
        driver.implicitly_wait(3)

        #Show All iphones
        link = driver.find_element(By.XPATH, show_all_xpath)
        link.click()
        driver.implicitly_wait(3)

    pass

#MAIN FUNCTION
def iPhoneScraperMain():
    print ("Web Scraper in progress, please wait...")
    go_to_o2()
    print ("We are scraping from the O2 Website...")
    print("Please hold on...")
    print("----------------------------------------------")
    print("INFO: If you get the below error, please re-run the script.")
    print("selenium.common.exceptions.WebDriverException: Message: target frame detached")
    print("----------------------------------------------")
    iphone_data_collector()
    print ("Creating CSV file")
    create_csv()
    print ("Creating a beautiful graph.")
    make_graph()
    print("Sorry for the wait, all done now :)")
    driver.quit()

if __name__ == "__main__":
    iPhoneScraperMain()
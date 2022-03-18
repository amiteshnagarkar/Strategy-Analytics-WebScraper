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

from selenium.webdriver.chrome.options import Options


#RE-RUN IF U GET THIS ERROR - selenium.common.exceptions.WebDriverException: Message: target frame detached
#Todo: debug and fix later.

#Need to store this as an environmental variable
PATH = Service("./driver/chromedriver")

#Global
show_all_xpath = "/html/body/div[2]/div[3]/div/div/div/article/div/div[4]/button"
driver = webdriver.Chrome(service=PATH)
simPlanNameList = []

def GoToEe():
    print('Inside GoToEe');
    eeWebsite = "https://shop.ee.co.uk/sim-only"
    iframeAcceptCookiesClass = "truste_popframe"
    viewAllSimPlans = "/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/button"

    driver.get(eeWebsite)
    driver.implicitly_wait(10)
    print('Finding iframe :' + str(iframeAcceptCookiesClass));
    iframe = driver.find_element(By.CLASS_NAME, iframeAcceptCookiesClass)
    print('Frame = ' + str(iframe));
    driver.switch_to.frame(iframe)
    link = driver.find_element(By.CLASS_NAME, "call")
    print('Trying to accept cookies..');
    link.click();
    driver.switch_to.parent_frame()
    
    driver.implicitly_wait(10)
    #View All Sim Plans
    link = driver.find_element(By.XPATH, viewAllSimPlans)
    driver.execute_script("arguments[0].scrollIntoView();",link)
    driver.execute_script("arguments[0].click();", link)
    #link.click()
    driver.implicitly_wait(10)
   

def SimOnlyDataCollector():

    OneGbData = "/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div[3]/button"
    OneSixtyGBData = "/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[3]/button"
    TwoHundredGBData = "/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/div[2]/div/div/div[3]/button"
    UnlimitedGBData = "/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div/div/div[1]/div/div[2]/div/div/div[3]/button"

    simOnlyXpaths = [OneGbData, OneSixtyGBData, TwoHundredGBData, UnlimitedGBData]
    driver.switch_to.default_content()

    image_counter = 0
    for sims in range(len(simOnlyXpaths)):

        #Select Specific Sim

        print("1")
        driver.implicitly_wait(3)
        print("2")
        link = driver.find_element(By.XPATH, simOnlyXpaths[sims])
        print("3")

        driver.execute_script("arguments[0].scrollIntoView();",link)
        driver.execute_script("arguments[0].click();", link)        

        #link.click()
        driver.implicitly_wait(3)

        #Get Sim Plan Information
        simPlanName = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div[2]/div/div[2]/section/div/article/div[1]/div/div[1]/div[2]/small[2]').text
        driver.implicitly_wait(3)
        simMonthlyCost = driver.find_element(By.CSS_SELECTOR, 'strong.c25-cart__package-pay-monthly-value').text
        simMonthlyCost = simMonthlyCost.lstrip('£')
        driver.implicitly_wait(3)
        simCoverageInfo = driver.find_element(By.CSS_SELECTOR, 'p.notification__text').text
        driver.implicitly_wait(3)

        #Add Collected Information to List
        simPlanNameList.append([simPlanName, simMonthlyCost, simCoverageInfo])

        #Screenshot
        image_filename = 'images/EE_Sim_Only_Screens/images/screenshot_' + str(simPlanName) + '_' + str(image_counter) + '.png'
        driver.save_screenshot(image_filename)
        image_counter += 1

        #Remove Plan
        driver.implicitly_wait(3)
        link = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/main/div[2]/div/div[2]/section/div/article/div[1]/div/div[2]/form/a')
        #link.click()
        driver.execute_script("arguments[0].scrollIntoView();",link)
        driver.execute_script("arguments[0].click();", link)

        #Click on SIM ONLY on homepage
        driver.implicitly_wait(3)
        link = driver.find_element(By.XPATH, '/html/body/div[2]/div[5]/main/div[3]/div[2]/div/div/div/div/div/div[3]/div/div/section/section[1]/div/div/div/div/div/div/div[1]/div/div[3]/div/a/img')
        #link.click()
        driver.execute_script("arguments[0].scrollIntoView();",link)
        driver.execute_script("arguments[0].click();", link)

        #View All Sim Plans
        driver.implicitly_wait(3)
        link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/button')
        #link.click()
        driver.execute_script("arguments[0].scrollIntoView();",link)
        driver.execute_script("arguments[0].click();", link)
        driver.implicitly_wait(5)

    
    pass


def CreateCsv():
    dataFrame = panda.DataFrame(simPlanNameList, columns=["Sim_Plan_Name", "Monthly_Cost", "Coverage Info"])
    dataFrame.to_csv('EE_Sim_Only_Plans.csv', index=False)


def MakeGraph():
    dataFrame = panda.read_csv('EE_Sim_Only_Plans.csv')
    ax = dataFrame.set_index('Sim_Plan_Name').plot()
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    plot.autoscale(enable=True, axis='both', tight=None)
    plot.savefig('EE_Sim_Only_Plans_Graph.png')
    


#MAIN FUNCTION
def SimOnlyScraperMain():
    print ("Web Scraper in progress, please wait...")
    GoToEe()
    print ("We are scraping from the EE Website...")
    print("INFO: If you get the below error, please re-run the script.")
    print("selenium.common.exceptions.WebDriverException: Message: target frame detached")
    SimOnlyDataCollector()
    print ("Creating CSV file")
    CreateCsv()
    print ("Creating a beautiful graph.")
    MakeGraph()
    print("Sorry for the wait, all done now :)")
    driver.quit()

if __name__ == "__main__":
    SimOnlyScraperMain()
    
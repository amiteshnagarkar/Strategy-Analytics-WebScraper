
'''
Amitesh Nagarkar

Description: Program to get all Data related Job Titles from the Inspiring Interns website to an excel document.

'''
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd

'''
Function: ScrapeDataJobs - Takes job title as a parameter and searches for jobs with data in their title.
'''
def scrapeDataJobs(job_titles):
  dataJobs = []
  
  filterredDataJobs = list(filter(lambda x: "Data" in x, job_titles))
  numberOfJobs = len(job_titles);

  for title in filterredDataJobs[:numberOfJobs]:
    dataJobs.append(title)
    df = pd.DataFrame(dataJobs)
    excelWriter = pd.ExcelWriter('InspiringInterns-DJ.xlsx', engine='xlsxwriter')
    df.to_excel(excelWriter, sheet_name='Data Jobs', index=False)
    excelWriter.save()

'''
Function: scrapeJobTitles - Scrapes for H1 tag on the Inspiring Interns job-board site & pulls all job titles.
'''
def scrapeJobTitles(totalPages):
  print('Started.. hold on...');
  job_titles = []
  pageCounter = 1
  while pageCounter != totalPages:
      url = f"https://www.inspiringinterns.com/job-board/all?page={pageCounter}"
      response = requests.get(url)
      htmlContent = response.content
      soup = BeautifulSoup(htmlContent, "html.parser")
      for h1Tag in soup.find_all("h1", class_="hide-for-mobile"):
            job_titles.append(h1Tag.get_text(strip=True))
      pageCounter += 1;
  return job_titles;

'''
Main module to start scraping.
'''
def startScraping():
    print('Starting scraping. Looking for Data jobs on Inspiring Interns....Please wait');
    job_titles = scrapeJobTitles(50); #50 jobs at the moment but can be scrapped for actual value
    scrapeDataJobs(job_titles);
    print('Done!. Scraping data is available at : InspiringInterns-DJ.xlsx');

if __name__ == "__main__":
  startScraping();
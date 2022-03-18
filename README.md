<div id="top"></div>

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://www.strategyanalytics.com/">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Strategy Analytics Skills Test 2022</h3>

  <p align="center">
    <br />
    <a href="linkedin.com/in/amitesh-nagarkar-506941117">View O2 Demo</a>
     <a href="linkedin.com/in/amitesh-nagarkar-506941117">View EE Demo</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#notes">Notes</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

[![Screen Shot][product-screenshot]](https://www.linkedin.com/in/amitesh-nagarkar-506941117/)

Python web-scraping scripts that get data from the O2 and EE website.

O2 Script:
* Gets all Pay Monthly iPhone data (Phone Name, Model & Month, Upfront Cost, Monthly Cost, Data (need to update code), First Offer) - at default capacity, default colour, O2's top pick plan, no extras, no spend cap, no extras, no accessories, no trade in - includes CSV, Graph and Screenshots.

EE Script:
* Gets the following Pay Monthly SIM Only 24 Month Contracts (Sim Plan Name, Monthly Cost, Coverage Information) - 1GB Data, 160GB Data, 200GB Data - includes CSV, Graph and Screenshots.

<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

* [Python](https://www.python.org/)
* [Selenium](https://www.selenium.dev/)
* [Pandas](https://pandas.pydata.org/docs/index.html#)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Make sure you have the following prerequisites on your development machine.
* Python3, Pip, Git, Chrome Browser. I would also recommend using a virtual env.
* The Chromedriver used is available in the repository in driver folder. The scripts assumes the driver is available in this current folder.

### Installation

How to run the two scripts (Please note: the .csv and graph are generated in the current directory and the images are generated in the images directory):

1. Clone the repo
   ```sh
   git clone https://github.com/amiteshnagarkar/Strategy-Analytics-WebScraper
   ```
2. Install packages
   ```sh
   pip install -r requirements.txt
   ```
3. Run the O2 Script
   ```sh
   python3 O2_Script.py
   ```   
4. Run the EE Script
   ```sh
   python3 EE_Script.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Amitesh Nagarkar - [@amiteshnagarkar](https://www.linkedin.com/in/amitesh-nagarkar-506941117/)

Project Link: [https://github.com/amiteshnagarkar/Strategy-Analytics-WebScraper](https://github.com/amiteshnagarkar/Strategy-Analytics-WebScraper)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- NOTES -->
## Notes

* The O2/EE website can change. The relative XPath will need to be altered as the script may not work as expected. Please view the demo if this is the case.

Further enhancements I would make in a commerical enviornment: 
* Refrain from using time.sleep()
* Set Browser zoom level to 100 percent.
* Refrain from using XPATH - as changes in the UI of the target site would mean these scripts will not function. Use CSSSELECTOR OR ID (would allow more data to be collected, more efficently, rather than harcoding the element).
* Use a design pattern.
* Write tests!
* Carry out further data cleansing.

Known Problems: 
* First run may take some time as the chromedriver may need time to load.
* Re-run if you get this error : selenium.common.exceptions.WebDriverException: Message: target frame detached

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Thanks Strategy Analytics for this opportunity. Hope to work on projects like these, in a commercial environment, where I can gather more data, create more visually appealing, complex, but easy to understand, graphs.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/amitesh-nagarkar-506941117/
[product-screenshot]: images/screenshot.png

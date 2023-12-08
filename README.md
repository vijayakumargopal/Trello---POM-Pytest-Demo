Trello Website Automation For Demo 

Technologies Used: Python, Pytest, Selenium, PyTest, POM

Selenium - Pytest:
  Selenium is a module to do the web automation. Pytest is framework which will give you the structure of the execution

POM
  Page Object Model used to maintain the clear code base

Folder wise Explanation

Data: 
  Inputs for your test like browser name, credentials, environment, URL, etc.,
  In this project, JSON file only presents, you can use multiple environments like, excel sheet, sqlite3 db, text file, ini file, etc., based on the requirement

Drivers: 
  Driver file for all the browser to trigger the browser

Locators:

  locators contains multiple python module which is used to store the locators of the each pages

Pages:

  Pages folder contains multiple python module. Each module contains the each page actions like entering data, clicking button, drag and drop, validating label, etc.,

  Note: basic_browser_actions.py  This file contains more than 70+ keywords for web automation. You have to inherit this class into your pages and you can use all actions from here.

Tests:

  Test folder contains test cases of the each pages. 

Reports:

  Multiple type of reports generating.
  1. HTML report with screen shot for failure using pytest
  2. Video recording using pyautogui
  3. log file using logger module

Utilities:

  Utility folder to write the python functions for your testing, fetching, api requests send, reading Input file, etc.,
  

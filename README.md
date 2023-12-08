# Trello Web Automation

This repository contains a web automation script for automating actions on the Trello website using Python, Pytest, the Page Object Model (POM) pattern, and Selenium WebDriver.

## Project Structure

The project is organized into the following folders:

- **drivers:** Contains browser drivers for different web browsers.
  
- **pages:** Includes page action modules, each representing a specific page on the Trello website.
  
- **locators:** Holds locator modules for each page, containing web element locators.
  
- **utilities:** Contains Python functions for various utility purposes, such as reading input files, recording videos, implementing logging mechanisms, etc.

- **input_datas:** Stores input data for tests, including credentials, browser environment details, and other essential data.

- **tests:** Consists of test cases using Pytest, leveraging the POM pattern for better code organization.

## Technologies Used

- **Python:** The primary programming language for scripting automation tasks.

- **Pytest:** A testing framework for running test cases.

- **Page Object Model (POM) pattern:** A design pattern for organizing and managing page actions and locators.

- **Selenium WebDriver:** A powerful tool for automating web browsers.

## Keywords for Web Automation

This project includes a rich set of keywords for web automation, making it easy to express various actions in your test cases. Here are some of the key keywords available in the project:
You can see all the keywords, arguments and returned data explained in basic_actions.html file.


- **click:** Simulate a click action on a web element.

- **type:** Enter text into input fields.

- **drag and drop:** Perform a drag-and-drop operation on web elements.

- **element should be visible:** Check if a specific element is visible on the page.


## How to Use Keywords

These keywords are conveniently organized within the `pages` folder. Each page module contains methods that leverage these keywords to perform specific actions on the corresponding web page.

Example:

```python
# pages/home_page.py

from pages.basic_browser_actions import BasicActions
from selenium.webdriver.common.by import By

class HomePage(BasicActions):

    email_entry = (By.ID, "email-input")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_email_id(self, email_id):
        self.wait_for_object(email_entry, 10)
        self.type_words(email_entry, email_id)
       

## Getting Started

1. Clone this repository to your local machine.

```bash
git clone https://github.com/vijayakumargopal/Trello---POM-Pytest-Demo.git
cd trello-web-automation

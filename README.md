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

## Getting Started

1. Clone this repository to your local machine.

```bash
git clone https://github.com/your-username/trello-web-automation.git
cd trello-web-automation

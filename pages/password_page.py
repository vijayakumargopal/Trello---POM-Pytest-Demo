from pages.basic_browser_actions import BasicActions
from locators.password_page_locators import PasswordLocators
from pages.home_page import HomePage
import time
from selenium.webdriver.common.by import By


class PasswordPage(BasicActions, PasswordLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.all_prod_trello = (By.XPATH, '//div[@data-testid="start-product__TRELLO_TRELLO"]')

    def verify_email_label(self, email_id):
        self.check_text_of_object(self.email_id_label, email_id)

    def enter_password(self, password):
        self.wait_for_object(self.password_entry_box)
        time.sleep(2)
        self.type_words(self.password_entry_box, password)

    def click_login_button(self):
        self.click_me(self.login_button)
        if self.element_displayed(self.all_prod_trello, 5):
            self.click_me(self.all_prod_trello)
        home_page = HomePage(self.driver)
        home_page.verify_header_label()
        return home_page


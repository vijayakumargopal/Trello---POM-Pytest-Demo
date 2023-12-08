from pages.basic_browser_actions import BasicActions
from locators.email_page_locators import EmailPageLocators
from pages.password_page import PasswordPage


class EmailPage(BasicActions, EmailPageLocators):

    """ This class represents the actions of the email page and its locators """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_header(self):
        self.wait_for_object(self.login_to_continue_header)

    def click_continue_button(self):
        self.click_me(self.continue_button)

    def enter_email_id(self, email_id):
        self.wait_for_object(self.email_id_entry_box)
        self.type_words(self.email_id_entry_box, email_id)
        self.click_continue_button()
        password_page = PasswordPage(self.driver)
        password_page.verify_email_label(email_id)
        return password_page

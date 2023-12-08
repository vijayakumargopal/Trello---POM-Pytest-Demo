from locators.board_page_locators import BoardPageLocators
from pages.basic_browser_actions import BasicActions
from selenium.webdriver.common.by import By


""" This page class contains all the methods related to the board page of the application """

class BoardPage(BasicActions, BoardPageLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_board_title(self, board_name):
        self.check_text_of_object(self.board_title, board_name)

    def add_card_button(self, list_name, card_name):
        self.click_me(self.add_another_list_button)
        self.wait_for_object((By.XPATH, f'//h2[text()="{list_name}"]/ancestor::li//a[text()="{card_name}"]'))

    def add_card_in_to_do_section(self, card_name):
        self.click_me(self.to_do_add_card_button)
        self.type_words(self.new_card_name_entry, card_name)
        self.add_card_button("To Do", card_name)

    def add_card_in_doing_section(self, card_name):
        self.click_me(self.doing_add_card_button)
        self.type_words(self.new_card_name_entry, card_name)
        self.add_card_button("Doing", card_name)

    def add_card_in_done_section(self, card_name):
        self.click_me(self.done_add_card_button)
        self.type_words(self.new_card_name_entry, card_name)
        self.add_card_button("Done", card_name)

    def drag_card_drop_card(self, card_name, list1, list2):
        src_element = f'//h2[text()="{list1}"]/ancestor::li/div/ol//a[text()="{card_name}"]'
        target_element = f'//h2[text()="{list2}"]/ancestor::li/div/ol'
        self.drag_and_drop((By.XPATH, src_element), (By.XPATH,target_element))

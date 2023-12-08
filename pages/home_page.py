from locators.home_page_locators import HomeLocators
from pages.basic_browser_actions import BasicActions
from pages.board_page import BoardPage


""" This page class contains all the methods related to the home page of the application """

class HomePage(BasicActions, HomeLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_header_label(self):
        self.wait_for_object(self.workplace_label)

    def click_create_board_button(self):
        self.click_me(self.create_board_button)

    def enter_new_board_name(self, board_name):
        self.wait_for_object(self.board_title_input_box)
        self.type_words(self.board_title_input_box, board_name)

    def click_create_board_submit_button(self):
        self.click_me(self.create_board_submit_button)
        board_page = BoardPage(self.driver)
        board_page.wait_for_object(board_page.board_title)
        board_page.click_me(board_page.cancel_button)
        return board_page


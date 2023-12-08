import pytest
from pages.email_page import EmailPage


class TestHomePage:

    @pytest.mark.usefixtures("open_browser_test_startup")
    def test_verify_home_page(self):
        """
        To Run this test: pytest -k test_verify_home_page
        Requirement Covered:
            JIRA-3035
        """

        email_page = EmailPage(self.driver)
        password_page = email_page.enter_email_id("vijayakumar.gopalbanu@gmail.com")
        password_page.enter_password("Vijay@123")
        home_page = password_page.click_login_button()
        home_page.verify_header_label()
        home_page.click_create_board_button()
        home_page.enter_new_board_name("Test Board")
        board_page = home_page.click_create_board_submit_button()
        board_page.verify_board_title("Test Board")

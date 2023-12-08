import pytest
from pages.email_page import EmailPage


"""
Requirements Covered:
    JIRA-3031, JIRA-3032, JIRA-3033, JIRA-3034
"""


class TestEmailPage:

    @pytest.mark.usefixtures("open_browser_test_startup")
    def test_empty_email_id_error_message(self):
        """
        To Run this test: pytest -k test_empty_email_id_error_message
        Requirement Covered:
            JIRA-3031
        """
        email_page = EmailPage(self.driver)
        email_page.click_continue_button()
        email_page.verify_error_message()


    @pytest.mark.usefixtures("open_browser_test_startup")
    def test_signup_reset_button_visible(self):
        """
        To Run this test: pytest -k test_signup_reset_button_visible
        Requirement Covered:
            JIRA-3032
        """
        email_page = EmailPage(self.driver)
        email_page.verify_create_account_button_is_present()
        email_page.verify_cannot_login_link_is_present()


    @pytest.mark.usefixtures("open_browser_test_startup")
    def test_verify_email_id_label(self):
        """
        To Run this test: pytest -k test_verify_email_id_label
        Requirement Covered:
            JIRA-3033
        """
        email_page = EmailPage(self.driver)
        email_page.enter_email_id("vijayakumar.gopalbanu@gmail.com")

    @pytest.mark.usefixtures("open_browser_test_startup")
    def test_title_of_the_page(self):
        """
        To Run this test: pytest -k test_title_of_the_page
        Requirement Covered:
            JIRA-3034
        """
        email_page = EmailPage(self.driver)
        title_presents = email_page.get_window_title()
        assert title_presents == email_page.page_title

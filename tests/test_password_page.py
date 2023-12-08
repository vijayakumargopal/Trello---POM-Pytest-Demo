import pytest
from pages.email_page import EmailPage
from pages.password_page import PasswordPage


class TestPasswordPage:

    @pytest.mark.usefixtures("open_browser_test_startup")
    def test_verify_password_page(self):
        """
        To Run this test: pytest -k test_verify_password_page
        Requirement Covered:
            JIRA-3034
        """
        email_page = EmailPage(self.driver)
        password_page = email_page.enter_email_id("vijayakumar.gopalbanu@gmail.com")
        password_page.enter_password("Vijay@123")
        password_page.click_login_button()


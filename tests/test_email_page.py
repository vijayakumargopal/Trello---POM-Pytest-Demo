import pytest
from pages.email_page import EmailPage


class TestEmailPage:

    @pytest.mark.usefixtures("open_browser_test_startup")
    def test_verify_email_page(self):
        """
        To Run this test: pytest -k test_verify_email_page
        Requirement Covered:
            JIRA-3032
        """
        email_page = EmailPage(self.driver)
        email_page.verify_header()


    @pytest.mark.usefixtures("open_browser_test_startup")
    def test_verify_email_id_label(self):
        """
        To Run this test: pytest -k test_verify_email_id_label
        Requirement Covered:
            JIRA-3033
        """
        email_page = EmailPage(self.driver)
        email_page.enter_email_id("vijayakumar.gopalbanu@gmail.com")

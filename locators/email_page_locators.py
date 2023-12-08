from selenium.webdriver.common.by import By


class EmailPageLocators:

    """ A class for email page locators. All email page locators should come here """
    
    login_to_continue_header = (By.XPATH, "//h5[text()='Log in to continue']")
    email_id_entry_box = (By.NAME, "username")
    continue_button = (By.ID, "login-submit")
    cannot_login = (By.ID, "resetPassword")
    create_account = (By.ID, "signup")
    error_enter_email_id = (By.ID, "username-uid2-error")
    page_title = "Log in to continue - Log in with Atlassian account"
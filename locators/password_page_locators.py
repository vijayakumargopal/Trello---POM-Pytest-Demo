from selenium.webdriver.common.by import By


class PasswordLocators:

    email_id_label = (By.CLASS_NAME, "css-eznkzx")
    password_entry_box = (By.ID, "password")
    password_eye_icon = (By.CLASS_NAME, "css-g42x0s")
    login_button = (By.ID, "login-submit")


from selenium.webdriver.common.by import By


class HomeLocators:

    workplace_label = (By.XPATH, '//h3[text()="YOUR WORKSPACES"]')
    create_board_button = (By.XPATH, '//li[@data-testid="create-board-tile"]')
    board_title_input_box = (By.XPATH, '//input[@data-testid="create-board-title-input"]')
    create_board_submit_button = (By.XPATH, '//button[text()="Create"]')

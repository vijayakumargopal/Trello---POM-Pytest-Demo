from selenium.webdriver.common.by import By


class BoardPageLocators:

    board_title = (By.XPATH, '//h1[@data-testid="board-name-display"]')
    add_another_list_button = (By.XPATH, '//button[@data-testid="list-composer-button"]')
    to_do_add_card_button = (By.XPATH, '//h2[text()="To Do"]/ancestor::li//button[@data-testid="list-add-card-button"]')
    doing_add_card_button = (By.XPATH, '//h2[text()="Doing"]/ancestor::li//button[@data-testid="list-add-card-button"]')
    done_add_card_button = (By.XPATH, '//h2[text()="Done"]/ancestor::li//button[@data-testid="list-add-card-button"]')
    new_card_name_entry = (By.XPATH, '//textarea[@placeholder="Enter a title for this card…"]')
    add_card_button = (By.XPATH, '//button[text()="Add card"]')
    cancel_button = (By.XPATH, '//button[contains(@aria-label, "Cancel")]')

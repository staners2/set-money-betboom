from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.BetListPage import BetListPage


class LoginPage:
    OPEN_LOGIN_MENU_BUTTON_ID = "header_login_btn"  # ID
    NUMBER_FIELD_XPATH = "//input[@placeholder='Номер телефона']"
    PASSWORD_FIELD_XPATH = "//input[@type='password']"
    LOGIN_IN_ACCOUNT_BUTTON_ID = "modal_login_btn"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_login_menu(self):
        login_button = self.driver.find_element(By.ID, self.OPEN_LOGIN_MENU_BUTTON_ID)
        login_button.click()

    def input_number(self, number: str):
        number_field = self.driver.find_element(By.XPATH, self.NUMBER_FIELD_XPATH)
        number_field.click()
        for letter in number:
            number_field.send_keys(letter)

    def input_password(self, password: str):
        password_field = self.driver.find_element(By.XPATH, self.PASSWORD_FIELD_XPATH)
        for letter in password:
            password_field.send_keys(letter)

    def login_account(self) -> BetListPage:
        login_button = self.driver.find_element(By.ID, self.LOGIN_IN_ACCOUNT_BUTTON_ID)
        login_button.click()

        return BetListPage(self.driver)

import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import Config

block_bet: WebElement | None = None

class MatchPage:

    BLOCK_MAP_XPATH = '//div[contains(text(), "{0}")]'
    BLOCK_LEFT_COMMAND_TITLE = './div/div[1]/div[1]/div'
    BLOCK_COMMAND_BET = './div/div[2]/div[{0}]/button'

    INPUT_MONEY_FIELD_XPATH = '//*[@id="__next"]/div/div[3]/div/div[4]/div/div[1]/div/div/div'
    ACCEPT_SET_MONEY = '//div[contains(text(), "Сделать ставку")]'

    DOTA_2_ITEM_XPATH = '//*[@id="__next"]/div/div[1]/nav/div[2]/button/div[2]/label'
    COMMAND_ITEM_IN_LIST_XPATH = '//div[@title="{0} против {1}"]'
    LIVE_TRANSLATION_ITEM_XPATH = '//*[@id="__next"]/div/div[2]/div/nav/div[1]/a[2]'
    ODIN_IFRAME = '//*[@id="oddin_div_iframe"]/iframe'

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def select_bet_on_match(self, map: str, command_win: str):
        global block_bet
        time.sleep(10)
        map_elements = self.driver.find_elements(By.XPATH, self.BLOCK_MAP_XPATH.format(map))

        map_element: WebElement

        for map_element in map_elements:
            # получить родителя
            type_of_bet_element = map_element.find_element(By.XPATH, "..")
            print(type_of_bet_element.text)
            if type_of_bet_element.text.__contains__("Исход с учетом доп раундов"):
                print("Block is found!")
                block_bet = type_of_bet_element.find_element(By.XPATH, "..")
                break

        # Делаем ставку на левую команду
        if block_bet.find_element(By.XPATH, self.BLOCK_LEFT_COMMAND_TITLE).text == command_win:
            block_bet.find_element(By.XPATH, self.BLOCK_COMMAND_BET.format(1)).click()
        # Делаем ставку на правую команду
        else:
            block_bet.find_element(By.XPATH, self.BLOCK_COMMAND_BET.format(2)).click()


    def input_money_in_field(self, price: int):
        div_money_field = self.driver.find_element(By.XPATH, self.INPUT_MONEY_FIELD_XPATH)
        div_money_field.click()
        input_money_field = div_money_field.find_element(By.XPATH, "../input")
        input_money_field.send_keys(price)


    def accept_set_money(self):
        accept_money_field = self.driver.find_element(By.XPATH, self.ACCEPT_SET_MONEY)
        accept_money_field.click()
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import Config
from pages.MatchPage import MatchPage


class BetListPage:

    DOTA_2_ITEM_XPATH = '//*[@id="__next"]/div/div[1]/nav/div[2]/button/div[2]/label'
    COMMAND_ITEM_IN_LIST_XPATH = "//div[@title='{0} против {1}']"
    LIVE_TRANSLATION_ITEM_XPATH = '//*[@id="__next"]/div/div[2]/div/nav/div[1]/a[2]'
    ODIN_IFRAME = '//*[@id="oddin_div_iframe"]/iframe'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        iframe = driver.find_element(By.XPATH, self.ODIN_IFRAME)
        self.driver.switch_to.frame(iframe)

    def select_live_translation(self):
        while True:
            try:
                WebDriverWait(self.driver, Config.WAIT_TIME).until(
                    expected_conditions.visibility_of_all_elements_located((By.XPATH, self.LIVE_TRANSLATION_ITEM_XPATH))
                )
                elem = self.driver.find_element(By.XPATH, self.LIVE_TRANSLATION_ITEM_XPATH)
                elem.click()
                break
            except:
                pass

    def select_dota2_filter(self):
        while True:
            try:
                WebDriverWait(self.driver, Config.WAIT_TIME).until(
                    expected_conditions.visibility_of_all_elements_located((By.XPATH, self.DOTA_2_ITEM_XPATH))
                )
                elem = self.driver.find_element(By.XPATH, self.DOTA_2_ITEM_XPATH)
                elem.click()
                break
            except:
                pass

    def open_menu_match(self, command_one: str, command_two: str) -> MatchPage:
        WebDriverWait(self.driver, Config.WAIT_TIME).until(
            expected_conditions.visibility_of_all_elements_located(
                (By.XPATH, self.COMMAND_ITEM_IN_LIST_XPATH.format(command_one, command_two))
            )
        )
        command_block = self.driver.find_element(
            By.XPATH, self.COMMAND_ITEM_IN_LIST_XPATH.format(command_one, command_two)
        )
        if command_block is None:
            command_block = self.driver.find_element(
                By.XPATH, self.COMMAND_ITEM_IN_LIST_XPATH.format(command_two, command_one)
            )
        print(command_block)
        command_block.click()

        return MatchPage(self.driver)

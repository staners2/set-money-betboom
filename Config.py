import os
from dotenv import load_dotenv

load_dotenv()

# Credentionals by account
NUMBER_ACCOUNT = os.getenv("NUMBER_ACCOUNT")
PASSWORD_ACCOUNT = os.getenv("PASSWORD_ACCOUNT")

# Count set money on bet
COUNT_SET_MONEY = 10

# Config selenium
BASE_URL = "https://betboom.ru/esport"
PATH_WEBDRIVER = "./chromedriver"
WAIT_TIME = 20

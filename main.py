import argparse
import logging
import platform
import sys
import time

from bottle import route, run, template
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


import Config
from pages.LoginPage import LoginPage


@route("/set-bet/<name>")
def index(name):
    return template("<b>Hello {{name}}</b>!", name=name)


def main(command_one: str, command_two: str, map: str, command_win_title: str, price: int):
    """
    :param command_one: 1 команда
    :param command_two: 2 команда
    :param map: название карты
    :param command_win_title: команда победитель
    :param price: сколько ставить
    :return:
    """
    # run(host="localhost", port=8080, debug=True)

    # ======== Настройки web driver'a =======
    # driver = webdriver.Chrome("./chromedriver")
    service = Service(Config.PATH_WEBDRIVER)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.execute_script("document.body.style.zoom='0.5'")
    driver.get(Config.BASE_URL)
    # =======================================

    login_page = LoginPage(driver)
    login_page.open_login_menu()
    login_page.input_number(Config.NUMBER_ACCOUNT)
    login_page.input_password(Config.PASSWORD_ACCOUNT)

    bet_list_page = login_page.login_account()
    bet_list_page.select_live_translation()
    bet_list_page.select_dota2_filter()

    match_page = bet_list_page.open_menu_match(command_one, command_two)
    try_count = 0
    while True:
        try:
            if try_count >= 4:
                logging.error("Не удалось найти карту для проставления ставки")
                break
            match_page.select_bet_on_match(map, command_win_title)
            break
        except:
            # TODO: Сделать scroll вниз экрана
            try_count += 1

    match_page.input_money_in_field(price)
    match_page.accept_set_money()

class RawTextArgumentDefaultsHelpFormatter(
        argparse.ArgumentDefaultsHelpFormatter,
        argparse.RawTextHelpFormatter
    ):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=('''\
              Скрипт заработка :)
        --------------------------------
            Утилита делающая ставки
            на сайте BetBoom
            по игре Dota2
        '''), formatter_class=RawTextArgumentDefaultsHelpFormatter)

    parser.add_argument('-one', '--command_one', dest="command_one", type=str, nargs=1, required=True,
                        help='Название первой команды', metavar="'Evil Geniuses'")

    parser.add_argument('-two', '--command_two', dest="command_two", type=str, nargs=1, required=True,
                        help='Название второй команды', metavar="'Team Liquid'")

    parser.add_argument('-m', '--map', dest="map", type=str, nargs=1,
                        choices=["Карта 1", "Карта 2", "Карта 3", "Карта 4", "Карта 5"], required=True,
                        help='Название карты', metavar="'Карта 1'")

    parser.add_argument('-w', '--win', dest="command_win", type=str, nargs=1, required=True,
                        help='Название команды победителя', metavar="'Evil Geniuses'")

    parser.add_argument('-p', '--price', dest="price", type=int, nargs='?', default=Config.COUNT_SET_MONEY,
                        help='Сколько ставить на победу?')

    args = parser.parse_args(sys.argv[1:])

    main(args.command_one, args.command_two, args.map, args.command_win, args.price)

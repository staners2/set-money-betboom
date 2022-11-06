# Название проекта: Автоматизация проставляения ставок на киберспорт

# Описание проекта
Скрипт позволяет делать ставки на сайте betboom.ru по дисциплине Dota2

# Требования к системе
**Окружение**  |  **Версия**   |
-------------- |---------------|
python         |   `3.10`      |
poetry         |   `1.1.13`    |
google browser |   `любой`     |
google driver  | `ссылка ниже` |

# Инструкция по скачиваниюю google driver
1. Зайти на сайт [selenium.dev](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)
2. В самом низу есть ссылка на скачивание Google Chrome драйвера
3. Положить этот драйвер в корень проекта
4. Зайти в Config.py и изменить переменную PATH_WEBDRIVER, указав путь до драйвера

# Окружение ENV
1. Скопировать .env.example в файл .env
2. Заполнить необходимые данные

# Структура проекта
Pages - набор страниц сайта и действий
main.py - точка входа

# Сборка проекта
```bash
poetry install
```

# Получение справки по запуску скрипта
```bash
poetry run python3 main.py -h
```

# Запуск скрипта
```bash
poetry run python3 main.py
```

Проект написан на python+django. БД - SQlite.

Для запуска необходимо выполнить:
1. Создать venv с python 3.10
2. Установить зависимости - pip install -r requirements.txt
3. Запуск сервера - ./manage.py runserver 8000
4. Тестовый скрипт для проверки запросов - api_test_requests.py
5. Запуск тестов - ./manage.py test validator.tests.test_api.ValidatorApiTestCase 

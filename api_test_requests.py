import requests


BASE_URL = 'http://127.0.0.1:8000/get_form/'


def api_test_requests():
    # проверка Employee_form
    url = BASE_URL + '?employee_email=alskdn@mail.ru&employee_phone=+7 999 999 99 99' \
                     '&employee_description=alskdn alsdn asd'
    resp = requests.post(url)

    print('Делаем запрос с параметрами: \nemployee_email=alskdn@mail.ru\nemployee_phone=+7 999 999 99 99\n'
          'employee_description=alskdn alsdn asd')
    print(f'Получаем название формы {resp.text}')

    # проверка Employee_form с количеством полей, большим, чем в форме
    url = BASE_URL + '?employee_email=alskdn@mail.ru&employee_phone=+7 999 999 99 99' \
                     '&employee_description=alskdn alsdn asd&employee_phone=+7 222 333 99 99'
    resp = requests.post(url)

    print('\nДелаем запрос с двумя employer_phone: \nemployee_email=alskdn@mail.ru\nemployee_phone=+7 999 999 99 99\n'
          'employee_description=alskdn alsdn asd\nemployee_phone=+7 222 333 99 99')
    print(f'Получаем название формы {resp.text}')

    # проверка Partner_form
    url = BASE_URL + '?partner_email=alskdn@mail.ru&partner_phone=+7 999 999 99 99' \
                     '&registration_date=2022-10-10'
    resp = requests.post(url)

    print('\nДелаем запрос с параметрами: \npartner_email=alskdn@mail.ru\npartner_phone=+7 999 999 99 99\n'
          'registration_date=2022-10-10')
    print(f'Получаем название формы {resp.text}')

    # проверка User_form
    url = BASE_URL + '?user_email=alskdn@mail.ru&user_phone=+7 999 993 92 99' \
                     '&order_date=10.12.2022&order_description=asldkmqawldkn2das'
    resp = requests.post(url)

    print('\nДелаем запрос с параметрами: \nuser_email=alskdn@mail.ru\nuser_phone=+7 999 993 92 99\n'
          'order_date=10.12.2022\norder_description=asldkmqawldkn2das')
    print(f'Получаем название формы {resp.text}')

    # проверка запроса, под который нет формы
    url = BASE_URL + '?email=alskdn@mail.ru&random_phone=+7 999 993 92 99' \
                     '&date=10.12.2022&order_description=asldkmqawldkn2das'
    resp = requests.post(url)

    print('\nДелаем запрос с полями, под которые нет формы: \nemail=alskdn@mail.ru\nrandom_phone=+7 999 993 92 99\n'
          'date=10.12.2022\norder_description=asldkmqawldkn2das')
    print(f'Получаем типизированные поля {resp.text}')


if __name__ == "__main__":
    api_test_requests()




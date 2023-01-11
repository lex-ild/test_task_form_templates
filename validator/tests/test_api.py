from django.urls import reverse
from rest_framework.test import APITestCase

from validator.models import FormTemplate, DataType


class ValidatorApiTestCase(APITestCase):
    def test_employee_form(self):
        test_form = FormTemplate.objects.create(
            name='Employee_form',
            form_data={
                'employee_email': DataType.EMAIL.value,
                'employee_phone': DataType.PHONE.value,
                'employee_description': DataType.TEXT.value
            },
        )
        test_form.save()

        url = reverse('find-template') + '?employee_email=alskdn@mail.ru&employee_phone=+7 999 999 99 99'\
                                         '&employee_description=alskdn alsdn asd'
        resp = self.client.post(url)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['name'], 'Employee_form')

    def test_employee_form_more_fields(self):
        test_form = FormTemplate.objects.create(
            name='Employee_form',
            form_data={
                'employee_email': DataType.EMAIL.value,
                'employee_phone': DataType.PHONE.value,
                'employee_description': DataType.TEXT.value
            },
        )
        test_form.save()

        url = reverse('find-template') + '?employee_email=alskdn@mail.ru&employee_phone=+7 999 999 99 99'\
                                         '&employee_description=alskdn alsdn asd&employee_phone=+7 222 333 99 99'
        resp = self.client.post(url)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['name'], 'Employee_form')

    def test_partner_form(self):
        test_form = FormTemplate.objects.create(
            name='Partner_form',
            form_data={
                'partner_email': DataType.EMAIL.value,
                'partner_phone': DataType.PHONE.value,
                'registration_date': DataType.DATE.value
            },
        )
        test_form.save()

        url = reverse('find-template') + '?partner_email=alskdn@mail.ru&partner_phone=+7 999 999 99 99'\
                                         '&registration_date=2022-10-10'
        resp = self.client.post(url)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['name'], 'Partner_form')

    def test_user_form(self):
        test_form = FormTemplate.objects.create(
            name='User_form',
            form_data={
                'user_email': DataType.EMAIL.value,
                'user_phone': DataType.PHONE.value,
                'order_date': DataType.DATE.value,
                'order_description': DataType.TEXT.value
            },
        )
        test_form.save()

        url = reverse('find-template') + '?user_email=alskdn@mail.ru&user_phone=+7 999 993 92 99'\
                                         '&order_date=10.12.2022&order_description=asldkmqawldkn2das'
        resp = self.client.post(url)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['name'], 'User_form')

    def test_not_found_form(self):
        test_form = FormTemplate.objects.create(
            name='User_form',
            form_data={
                'user_email': DataType.EMAIL.value,
                'user_phone': DataType.PHONE.value,
                'order_date': DataType.DATE.value,
                'order_description': DataType.TEXT.value
            },
        )
        test_form.save()

        url = reverse('find-template') + '?email=alskdn@mail.ru&random_phone=+7 999 993 92 99'\
                                         '&date=10.12.2022&order_description=asldkmqawldkn2das'
        resp = self.client.post(url)

        # проверяем, что вернулись правильные типы данных
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['email'], 'email')
        self.assertEqual(resp.data['random_phone'], 'phone')
        self.assertEqual(resp.data['date'], 'date')
        self.assertEqual(resp.data['order_description'], 'text')


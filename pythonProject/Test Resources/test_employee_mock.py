import unittest
from pip._vendor import requests
from unittest.mock import patch


class EmployeeMock:
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return f'{self.last}@yahoo.com'

    def pay_rise(self):
        return int(self.pay * self.raise_amount)

    def monthly_schedule(self, month):
        response = requests.get(f'https://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response !'


class TestEmployeeMock(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("The Sooner I Realize, The Better...")

    @classmethod
    def tearDownClass(cls):
        print("...That I'm Getting Closer")

    def setUp(self):
        self.employee1 = EmployeeMock("Sandy", "Bae", 20_000)
        self.employee2 = EmployeeMock("Mo", "Choo", 97_050)

    def tearDown(self):
        pass

    def test_firstname(self):
        self.assertEqual(self.employee1.fullname, "Sandy Bae")
        self.assertEqual(self.employee2.fullname, "Mo Choo")

        self.employee1.first = "Tamarr"
        self.employee2.last = "Tiwa"

        self.assertEqual(self.employee1.fullname, "Tamarr Bae")
        self.assertEqual(self.employee2.fullname, "Mo Tiwa")

    def test_email(self):
        self.assertEqual(self.employee1.email, "Bae@yahoo.com")
        self.assertEqual(self.employee2.email, "Choo@yahoo.com")

        self.employee1.last = "Tamarr"
        self.employee2.last = "Tiwa"

        self.assertEqual(self.employee1.email, "Tamarr@yahoo.com")
        self.assertEqual(self.employee2.email, "Tiwa@yahoo.com")

    def test_pay_rise(self):
        self.assertEqual(self.employee1.pay, 20_000)
        self.assertEqual(self.employee2.pay, 97_050)

        self.assertEqual(self.employee1.pay_rise(), 21_000)
        self.assertEqual(self.employee2.pay_rise(), 101_902)

    def test_monthly_schedule(self):
        with patch('test_employee_mock.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.employee1.monthly_schedule('May')
            mocked_get.assert_called_with('https://company.com/Bae/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False
            schedule = self.employee2.monthly_schedule('August')
            mocked_get.assert_called_with('https://company.com/Choo/August')
            self.assertEqual(schedule, 'Bad Response !')


if __name__ == '__main__':
    unittest.main()

import json


class Checking():

    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус кода"""
        assert status_code == result.status_code, f'\nОШИБКА, Статус-код не совпадает : {result.status_code}'
        print(f"\nУспешно! Статус код : {result.status_code}")
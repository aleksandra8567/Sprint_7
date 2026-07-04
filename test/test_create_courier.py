import requests
import allure
import pytest
from data import Data
from helpers import (
    create_random_login,
    create_random_password,
    create_random_firstname,
)

class TestCourierCreate:

    @allure.step("Формируем payload с валидными данными для создания курьера")
    def _get_valid_payload(self):
        return {
            'login': create_random_login(),
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }

    @allure.step("Формируем payload с заранее известным валидным логином (для проверки конфликта)")
    def _get_payload_with_taken_login(self):
        return {
            'login': Data.valid_login,
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }

    @allure.step("Отправляем POST-запрос на создание курьера")
    def _send_create_courier_request(self, payload):
        return requests.post(Data.URL_courier_create, data=payload)

    @allure.title('Проверка успешного создания аккаунта курьера с валидными данными')
    @allure.description('Проверяются код и тело ответа.')
    def test_create_courier_account_success(self):
        payload = self._get_valid_payload()
        response = self._send_create_courier_request(payload)

        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}. Ответ: {response.text}"
        assert response.json() == {'ok': True}, f"Неверный ответ тела: {response.json()}"

    @allure.title('Проверка получения ошибки при повторном использовании логина для создания курьера')
    @allure.description('Проверяются код и тело ответа.')
    def test_create_courier_account_login_taken_conflict(self):
        payload = self._get_payload_with_taken_login()
        response = self._send_create_courier_request(payload)

        expected_message = 'Этот логин уже используется. Попробуйте другой.'
        assert response.status_code == 409, f"Ожидался статус 409, получен {response.status_code}"
        assert response.json() == {'code': 409, 'message': expected_message}, f"Неверное тело ответа: {response.json()}"

    @allure.title('Проверка получения ошибки при создании курьера с незаполненными обязательными полями')
    @allure.description(
        'В тест по очереди передаются наборы данных с пустым логином или паролем. '
        'Проверяются код и тело ответа.'
    )
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password(), 'firstName': create_random_firstname()},
        {'login': create_random_login(), 'password': '', 'firstName': create_random_firstname()}
    ])
    def test_create_courier_account_with_empty_required_fields(self, empty_credentials):
        response = self._send_create_courier_request(empty_credentials)

        expected_message = 'Недостаточно данных для создания учетной записи'
        assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
        assert response.json() == {'code': 400, 'message': expected_message}, f"Неверное тело ответа: {response.json()}"
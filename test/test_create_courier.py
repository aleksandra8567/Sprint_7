import allure
import pytest
import logging
from data import Data
from helpers import (
    get_valid_courier_payload,
    get_payload_with_taken_login,
    create_random_login,
    create_random_password,
)
from api_client import ApiClient

logger = logging.getLogger(__name__)


class TestCourierCreate:

    @allure.title('Проверка успешного создания аккаунта курьера с валидными данными')
    @allure.description('Проверяются код и тело ответа при успешном создании курьера.')
    def test_create_courier_account_success(self):
        payload = get_valid_courier_payload()
        response = ApiClient.create_courier(Data.URL_COURIER_CREATE, payload)

        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        assert response.json() == {'ok': True}, f"Неверное тело ответа: {response.json()}"

    @allure.title('Проверка получения ошибки при повторном использовании логина для создания курьера')
    @allure.description('Проверяются код и тело ответа при конфликте логина.')
    def test_create_courier_account_login_taken_conflict(self):
        payload = get_payload_with_taken_login(Data.VALID_LOGIN)
        response = ApiClient.create_courier(Data.URL_COURIER_CREATE, payload)

        expected_message = 'Этот логин уже используется. Попробуйте другой.'
        assert response.status_code == 409, f"Ожидался статус 409, получен {response.status_code}"
        assert response.json() == {'code': 409, 'message': expected_message}, f"Неверное тело ответа: {response.json()}"

    @allure.title('Проверка получения ошибки при создании курьера с незаполненными обязательными полями')
    @allure.description(
        'В тест по очереди передаются наборы данных с пустым логином или паролем. '
        'Проверяются код и тело ответа.'
    )
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password(), 'firstName': 'Ivan'},
        {'login': create_random_login(), 'password': '', 'firstName': 'Petr'},
    ])
    def test_create_courier_account_with_empty_required_fields(self, empty_credentials):
        response = ApiClient.create_courier(Data.URL_COURIER_CREATE, empty_credentials)

        expected_message = 'Недостаточно данных для создания учетной записи'
        assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
        assert response.json() == {'code': 400, 'message': expected_message}, f"Неверное тело ответа: {response.json()}"
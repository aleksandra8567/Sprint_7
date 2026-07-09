import allure
import pytest
import logging
from data import Data
from helpers import (
    create_random_login,
    create_random_password,
)
from api_client import ApiClient

logger = logging.getLogger(__name__)


class TestCourierLogin:

    @allure.title('Проверка успешной аутентификации курьера при вводе валидных данных')
    @allure.description('Проверяются код и тело ответа.')
    def test_courier_login_success(self):
        response = ApiClient.courier_login(Data.URL_COURIER_LOGIN, Data.VALID_COURIER_DATA)

        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
        json_body = response.json()
        assert 'id' in json_body, f"В ответе отсутствует поле 'id'"

    @allure.title('Проверка получения ошибки аутентификации курьера при вводе невалидных данных')
    @allure.description(
        'В тест по очереди передаются наборы данных с несуществующим логином или неверным паролем. '
        'Проверяются код и тело ответа.'
    )
    @pytest.mark.parametrize('nonexistent_credentials', [
        {'login': create_random_login(), 'password': create_random_password()},
        Data.COURIER_DATA_WITH_WRONG_PASSWORD,
    ])
    def test_courier_login_nonexistent_data_not_found(self, nonexistent_credentials):
        response = ApiClient.courier_login(Data.URL_COURIER_LOGIN, nonexistent_credentials)

        expected_message = 'Учетная запись не найдена'
        assert response.status_code == 404, f"Ожидался статус 404, получен {response.status_code}"
        assert response.json() == {'code': 404, 'message': expected_message}, f"Неверное тело ответа"

    @allure.title('Проверка получения ошибки аутентификации курьера с пустым полем логина или пароля')
    @allure.description(
        'В тест по очереди передаются наборы данных с пустым логином или паролем. '
        'Проверяются код и тело ответа.'
    )
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password()},
        {'login': Data.VALID_LOGIN, 'password': ''},
    ])
    def test_courier_login_empty_credentials_bad_request(self, empty_credentials):
        response = ApiClient.courier_login(Data.URL_COURIER_LOGIN, empty_credentials)

        expected_message = 'Недостаточно данных для входа'
        assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
        assert response.json() == {'code': 400, 'message': expected_message}, f"Неверное тело ответа"
import requests
import allure
import pytest
from data import Data
from helpers import (
    create_random_login,
    create_random_password,
)

class TestCourierLogin:

    @allure.title('Проверка успешной аутентификации курьера при вводе валидных данных')
    @allure.description('Проверяются код и тело ответа.')
    def test_courier_login_success(self):
        response = requests.post(Data.URL_courier_login, data=Data.courier_data_without_name)

        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}. Ответ: {response.text}"
        assert 'id' in response.json(), f"В ответе отсутствует поле 'id'. Ответ: {response.json()}"

    @allure.title('Проверка получения ошибки аутентификации курьера при вводе невалидных данных')
    @allure.description(
        'В тест по очереди передаются наборы данных с несуществующим логином или неверным паролем. '
        'Проверяются код и тело ответа.'
    )
    @pytest.mark.parametrize('nonexistent_credentials', [
        {'login': create_random_login(), 'password': create_random_password()},
        Data.courier_data_with_wrong_password
    ])
    def test_courier_login_nonexistent_data_not_found(self, nonexistent_credentials):
        response = requests.post(Data.URL_courier_login, data=nonexistent_credentials)

        expected_message = 'Учетная запись не найдена'
        assert response.status_code == 404, f"Ожидался статус 404, получен {response.status_code}"
        assert response.json() == {'code': 404, 'message': expected_message}, f"Неверное тело ответа: {response.json()}"

    @allure.title('Проверка получения ошибки аутентификации курьера с пустым полем логина или пароля')
    @allure.description(
        'В тест по очереди передаются наборы данных с пустым логином или паролем. '
        'Проверяются код и тело ответа.'
    )
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password()},
        {'login': Data.valid_login, 'password': ''}
    ])
    def test_courier_login_empty_credentials_bad_request(self, empty_credentials):
        response = requests.post(Data.URL_courier_login, data=empty_credentials)

        expected_message = 'Недостаточно данных для входа'
        assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
        assert response.json() == {'code': 400, 'message': expected_message}, f"Неверное тело ответа: {response.json()}"
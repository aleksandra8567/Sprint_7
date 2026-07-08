import requests
import allure
from data import Data


class TestOrdersListGet:

    @allure.title('Проверка получения списка заказов')
    @allure.description('Проверяются код и тело ответа.')
    def test_orders_list_get_success(self):
        response = requests.get(Data.URL_ORDERS_LIST)
        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}. Ответ: {response.text}"
        assert type(response.json()['orders']) == list, "Поле 'orders' не является списком"
        assert len(response.json()['orders']) >= 0, "Список заказов пуст"
        if response.json()['orders']:
            assert 'id' in response.json()['orders'][0], "В первом элементе списка отсутствует поле 'id'"
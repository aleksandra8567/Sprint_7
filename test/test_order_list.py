import requests
import allure
from data import Data

class TestOrdersListGet:

    @allure.title('Проверка получения списка заказов')
    @allure.description('Проверяются код и тело ответа.')
    def test_orders_list_get_success(self):
        response = requests.get(Data.URL_orders_list)
        assert type(response.json()['orders']) == list and 'id' in response.json()['orders'][0]
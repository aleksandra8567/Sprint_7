import requests
import allure
import pytest
import json
from data import Data, OrderData

class TestOrderCreate:

    @allure.title('Проверка создания заказа с разными параметрами цвета')
    @allure.description(
        'Согласно требованиям, система должна позволять указать в заказе один цвет самоката, '
        'выбрать сразу оба или не указывать совсем. В тест по очереди передаются наборы данных '
        'с разными параметрами: серый, черный, оба цвета, цвет не указан. Проверяются код и тело ответа.'
    )
    @pytest.mark.parametrize('order_data', [
        OrderData.ORDER_DATA_GREY_1,
        OrderData.ORDER_DATA_BLACK_2,
        OrderData.ORDER_DATA_TWO_COLORS_3,
        OrderData.ORDER_DATA_NO_COLORS_4
    ])
    def test_order_create_color_parametrize_success(self, order_data):
        payload = json.dumps(order_data)
        headers = {'Content-Type': 'application/json'}

        response = requests.post(
            Data.URL_ORDERS_CREATE,
            data=payload,
            headers=headers,
            timeout=5
        )

        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}. Ответ: {response.text}"
        assert 'track' in response.text, f"В ответе отсутствует поле 'track'. Ответ: {response.text}"
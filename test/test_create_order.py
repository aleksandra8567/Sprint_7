import allure
import pytest
import logging
from data import Data, OrderData
from api_client import ApiClient

logger = logging.getLogger(__name__)


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
        OrderData.ORDER_DATA_NO_COLORS_4,
    ])
    def test_order_create_color_parametrize_success(self, order_data):
        response = ApiClient.create_order(Data.URL_ORDERS_CREATE, order_data)

        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        json_body = response.json()
        assert 'track' in json_body, f"В ответе отсутствует поле 'track'. Ответ: {response.text}"
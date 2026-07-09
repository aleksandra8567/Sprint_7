import logging
import pytest
from data import Data
from helpers import (
    create_random_login,
    create_random_password,
    create_random_firstname,
)
from api_client import ApiClient

logger = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def created_courier():
    login = create_random_login()
    password = create_random_password()
    first_name = create_random_firstname()

    payload_create = {
        "login": login,
        "password": password,
        "firstName": first_name,
    }

    resp_create = ApiClient.create_courier(Data.URL_COURIER_CREATE, payload_create)
    if resp_create.status_code != 201:
        raise RuntimeError(
            f"Не удалось создать курьера. Статус: {resp_create.status_code}, "
            f"ответ: {resp_create.text}"
        )

    payload_login = {
        "login": login,
        "password": password,
    }
    resp_login = ApiClient.courier_login(Data.URL_COURIER_LOGIN, payload_login)
    if resp_login.status_code != 200:
        raise RuntimeError(
            f"Не удалось получить id курьера через логин. Статус: {resp_login.status_code}, "
            f"ответ: {resp_login.text}"
        )

    response_data = resp_login.json()
    if not isinstance(response_data, dict) or "id" not in response_data:
        raise RuntimeError(
            f"Неожиданный формат ответа при логине курьера: {response_data}"
        )

    courier_id = response_data["id"]

    courier_data = {
        "login": login,
        "password": password,
        "firstName": first_name,
        "id": courier_id,
    }

    yield courier_data

    try:
        resp_delete = ApiClient.delete_courier(Data.URL_COURIER_DELETE_TEMPLATE, courier_id)
        if resp_delete.status_code not in (200, 204, 404):
            logger.warning(
                "Не удалось корректно удалить курьера %s. Статус: %s, ответ: %s",
                courier_id,
                resp_delete.status_code,
                resp_delete.text,
            )
    except Exception as e:
        logger.warning("Предупреждение: не удалось удалить курьера %s. Ошибка: %s", courier_id, e)
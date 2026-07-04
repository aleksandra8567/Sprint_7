import requests
import pytest
from data import Data
from helpers import (
    create_random_login,
    create_random_password,
    create_random_firstname,
)


@pytest.fixture(scope="function")
def created_courier():

    login = create_random_login()
    password = create_random_password()
    first_name = create_random_firstname()

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name,
    }

    resp_create = requests.post(Data.URL_courier_create, data=payload, timeout=10)

    assert resp_create.status_code == 201, (
        f"Не удалось создать курьера. Статус: {resp_create.status_code}, "
        f"ответ: {resp_create.text}"
    )

    response_data = resp_create.json()

    courier_id = login

    if isinstance(response_data, int):
        courier_id = response_data

    courier_data = {
        "login": login,
        "password": password,
        "firstName": first_name,
        "id": courier_id,
    }

    yield courier_data

    delete_url = f"{Data.BASE_URL}api/v1/courier/{courier_id}"

    try:
        resp_delete = requests.delete(delete_url, timeout=5)

        if resp_delete.status_code not in (200, 204, 404):
            assert False, f"Ошибка при удалении курьера. Статус: {resp_delete.status_code}, ответ: {resp_delete.text}"
    except Exception as e:

        print(f"Предупреждение: не удалось удалить курьера {courier_id}. Ошибка: {e}")

class Data:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"

    URL_COURIER_CREATE = f"{BASE_URL}api/v1/courier"
    URL_COURIER_LOGIN = f"{BASE_URL}api/v1/courier/login"
    URL_COURIER_DELETE_TEMPLATE = f"{BASE_URL}api/v1/courier/{{id}}"
    URL_ORDERS_CREATE = f"{BASE_URL}api/v1/orders"
    URL_ORDERS_LIST = f"{BASE_URL}api/v1/orders"

    VALID_LOGIN = "Sergo2611"
    VALID_PASSWORD = "qwerty"
    VALID_FIRSTNAME = "Ser"
    VALID_COURIER_DATA = {
        "login": "Sergo2611",
        "password": "qwerty",
        "firstName": "Sergo"
    }
    COURIER_DATA_WITHOUT_NAME = {
        "login": "Sergo2611",
        "password": "qwerty"
    }
    COURIER_DATA_WITH_WRONG_PASSWORD = {
        "login": "Sergo2611",
        "password": "123456"
    }

class OrderData:
    ORDER_DATA_GREY_1 = {
        "firstName": "Павел",
        "lastName": "Пашин",
        "address": "Открытое шоссе, 5к11",
        "metroStation": 8,
        "phone": "+78555555555",
        "rentTime": 3,
        "deliveryDate": "2024-09-16",
        "comment": "Хорошая погодка :)",
        "color": ["GREY"]
    }

    ORDER_DATA_BLACK_2 = {
        "firstName": "Костя",
        "lastName": "Костыгин",
        "address": "Большая Семёновская улица, 24",
        "metroStation": 10,
        "phone": "+78888888888",
        "rentTime": 5,
        "deliveryDate": "2024-09-18",
        "comment": "Ужаснено хочется покататься!",
        "color": ["BLACK"]
    }

    ORDER_DATA_TWO_COLORS_3 = {
        "firstName": "Илья",
        "lastName": "Илюшин",
        "address": "площадь Рогожская Застава, 2/1с2",
        "metroStation": 15,
        "phone": "+70009999999",
        "rentTime": 1,
        "deliveryDate": "2024-09-10",
        "comment": "Покатаемся!",
        "color": ["BLACK", "GREY"]
    }

    ORDER_DATA_NO_COLORS_4 = {
        "firstName": "Баба",
        "lastName": "Бабина",
        "address": "Волгоградский проспект, 28А",
        "metroStation": 20,
        "phone": "+78777777778",
        "rentTime": 2,
        "deliveryDate": "2024-09-17",
        "comment": "Едем",
        "color": []
    }

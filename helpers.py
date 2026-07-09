from faker import Faker
import logging

logger = logging.getLogger(__name__)

fake = Faker()
fakeRU = Faker(locale='ru_RU')

def create_random_login() -> str:
    login = fake.text(max_nb_chars=6).replace(" ", "") + str(fake.random_int(0, 999))
    logger.debug("Generated random login: %s", login)
    return login

def create_random_password() -> str:
    password = fake.password(
        length=10,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True
    )
    logger.debug("Generated random password: %s", password)
    return password

def create_random_firstname() -> str:
    firstname = fakeRU.first_name()
    logger.debug("Generated random firstName: %s", firstname)
    return firstname

def get_valid_courier_payload() -> dict:
    """Возвращает валидный payload для создания курьера (все поля заполнены)."""
    payload = {
        'login': create_random_login(),
        'password': create_random_password(),
        'firstName': create_random_firstname(),
    }
    logger.debug("Generated valid courier payload: %s", payload)
    return payload

def get_payload_with_taken_login(existing_login: str) -> dict:
    """Payload с заранее известным занятым логином (для проверки конфликта)."""
    payload = {
        'login': existing_login,
        'password': create_random_password(),
        'firstName': create_random_firstname(),
    }
    logger.debug("Generated payload with taken login (%s)", existing_login)
    return payload
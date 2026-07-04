from faker import Faker

fake = Faker()
fakeRU = Faker(locale='ru_RU')

def create_random_login() -> str:
    return fake.text(max_nb_chars=6).replace(" ", "") + str(fake.random_int(0, 999))

def create_random_password() -> str:
    return fake.password(
        length=10,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True
    )

def create_random_firstname() -> str:
    return fakeRU.first_name()
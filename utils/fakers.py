from faker import Faker
import random
from string import ascii_lowercase


fake = Faker(['ru_RU'])


# Функция для генерации пароля
def generate_random_string(length: int=10) -> str:
    return ''.join(random.choice(ascii_lowercase) for _ in range(length))

# Функция для генерации данных пользователя
def generate_user():
    return {
        'email': fake.email(),
        'password': generate_random_string(),
        'name': fake.name()
    }
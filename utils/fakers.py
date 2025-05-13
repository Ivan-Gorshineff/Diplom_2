import random

from faker import Faker
from string import ascii_lowercase


fake = Faker(['ru_RU'])


def generate_random_string(length: int=10) -> str:
    return ''.join(random.choice(ascii_lowercase) for _ in range(length))

def generate_user():
    return {
        'email': fake.email(),
        'password': generate_random_string(),
        'name': fake.name()
    }
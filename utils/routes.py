from enum import Enum


class ApiRoutes(str, Enum):

    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    REGISTER = f'{BASE_URL}/api/auth/register'
    LOGIN = f'{BASE_URL}/api/auth/login'
    UPDATE_USER = f'{BASE_URL}/api/auth/user'
    DELETE_USER = f'{BASE_URL}/api/auth/user'

    LIST_ORDERS = f'{BASE_URL}/api/orders'
    CREATE_ORDER = f'{BASE_URL}/api/orders'

    def __str__(self) -> str:
        return self.value
from http import HTTPStatus

from allure import title, description
import requests
from utils.data import *
from utils.routes import ApiRoutes
from conftest import get_user_token


class TestGetOrders:

    @title('Проверка получения заказа с авторизацией')
    @description('Тест проверяет, что можно получить заказы авторизированному пользователю')
    def test_get_orders_with_login(self, get_user_token):
        token = get_user_token
        response = requests.get(ApiRoutes.LIST_ORDERS, headers={'Authorization': f'{token}'})
        assert response.status_code == HTTPStatus.OK

    @title('Проверка получения заказа без авторизации')
    @description('Тест проверяет, что нельзя получить заказы авторизированному пользователю')
    def test_get_orders_without_login(self):
        response = requests.get(ApiRoutes.LIST_ORDERS)
        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert response.json()["message"] == ORDER_DONT_GET_WITHOUT_AUTH_MSG

import json
from http import HTTPStatus

from allure import title, description
import requests
from utils.data import *
from utils.routes import ApiRoutes
from conftest import get_user_token


class TestCreateOrder:

    @title('Проверка создания заказа с ингредиентами авторизованным пользователем')
    @description('Тест проверяет, что авторизованный пользователь может создать заказ, указав ингредиенты')
    def test_create_order_with_login_and_with_ingredients(self, get_user_token):
        token = get_user_token
        ingredients = (BIO_CUTLET_MAIN_ID, SPACE_SAUCE_ID, FLUORESCENT_BUN_ID, MINERAL_RINGS_MAIN_ID)
        burger = {
            "ingredients": ingredients
        }
        response = requests.post(ApiRoutes.CREATE_ORDER, headers={'Authorization': f'{token}'}, data=burger)
        assert response.status_code == HTTPStatus.OK

    @title('Проверка создания заказа с ингредиенами неавторизованным пользователем')
    @description('Тест проверяет, что авторизованный пользователь может создать заказ, указав ингредиенты')
    def test_create_order_without_login_and_with_ingredients(self):
        ingredients = (BIO_CUTLET_MAIN_ID, SPACE_SAUCE_ID, FLUORESCENT_BUN_ID, MINERAL_RINGS_MAIN_ID)
        burger = {
            "ingredients": ingredients
        }
        response = requests.post(ApiRoutes.CREATE_ORDER, data=burger)
        assert response.status_code == HTTPStatus.OK

    @title('Проверка создания заказа без ингридиентов')
    @description('Тест проверяет, что авторизованный пользователь не может создать заказ без ингредиентов, '
                'возвращается код 400 и сообщение об ошибке')
    def test_create_order_without_ingredients(self):
        ingredients = []
        burger = {
            "ingredients": ingredients
        }
        response = requests.post(ApiRoutes.CREATE_ORDER, data=burger)
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json()["message"] == CREATE_ORDER_WITHOUT_INGREDIENTS_MSG

    @title('Проверка создания заказа с некорректными ингридиентами')
    @description('Тест проверяет, что нельзя создать заказ, указав некорректные ингрединенты')
    def test_create_order_with_incorrect_ingredients(self):
        incorrect_ingredient = ['000000089']
        burger = {
            "ingredients": incorrect_ingredient
        }
        response = requests.post(ApiRoutes.CREATE_ORDER, data=burger)
        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR




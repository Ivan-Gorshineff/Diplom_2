from http import HTTPStatus

from allure import description, title
import requests
from utils import fakers, requests_api
from utils.requests_api import ApiRoutes
from utils.data import *


class TestCreateUser:

    @title('Проверка создания пользователя')
    @description('Тест проверяет, что при успешном создании пользователя возвращается код 200')
    def test_create_user_with_fill_fields(self):
        user_data = fakers.generate_user()
        response = requests.post(ApiRoutes.REGISTER, data=user_data)
        assert response.status_code == HTTPStatus.OK

    @title('Проверка создания пользователя, который уже зарегистрирован')
    @description('Тест проверяет, если пользователь существует, то вернется код 403 и сообщение об ошибке')
    def test_create_user_already_created_user(self):
        user_data = requests_api.create_user_and_get_user_data()
        response = requests.post(ApiRoutes.REGISTER, data=user_data)
        assert response.status_code == HTTPStatus.FORBIDDEN
        assert response.json()["message"] == USER_EXISTS_MSG

    @title('Проверка создания пользователя без заполненного поля "name"')
    @description('Тест проверяет, что при создании пользователя без name вернется код 403 сообщение об ошибке')
    def test_create_user_without_name(self):
        user_data = fakers.generate_user()
        email = user_data['email']
        password = user_data['password']
        incorrect_user_data = {
            'email': email,
            'password': password
        }
        response = requests.post(ApiRoutes.REGISTER, data=incorrect_user_data)
        assert response.status_code == HTTPStatus.FORBIDDEN
        assert response.json()["message"] == MISSING_FIELD_IN_USER_FORM_MSG

    @title('Проверка создания пользователя без заполненного поля "email"')
    @description('Тест проверяет, что при создании пользователя без "email" вернется код 403 сообщение об ошибке')
    def test_create_user_without_email(self):
        user_data = fakers.generate_user()
        name = user_data['name']
        password = user_data['password']
        incorrect_user_data = {
            'name': name,
            'password': password
        }
        response = requests.post(ApiRoutes.REGISTER, data=incorrect_user_data)
        assert response.status_code == HTTPStatus.FORBIDDEN
        assert response.json()["message"] == MISSING_FIELD_IN_USER_FORM_MSG

    @title('Проверка создания пользователя без заполненного "password"')
    @description('Тест проверяет, что при создании пользователя без "password" вернется код 403 сообщение об ошибке')
    def test_create_user_without_password(self):
        user_data = fakers.generate_user()
        email = user_data['email']
        name = user_data['name']
        incorrect_user_data = {
            'email': email,
            'name': name
        }
        response = requests.post(ApiRoutes.REGISTER, data=incorrect_user_data)
        assert response.status_code == HTTPStatus.FORBIDDEN
        assert response.json()["message"] == MISSING_FIELD_IN_USER_FORM_MSG

from http import HTTPStatus

from allure import title, description
import requests
from utils.data import *
from utils.routes import ApiRoutes
from utils import requests_api
from utils.fakers import fake, generate_random_string

class TestLoginUser:

    @title('Проверка логина существующего пользователя')
    @description('Тест проверяет, что пользователь может авторизоваться')
    def test_login_user_with_correct_credentials(self):
        user_data = requests_api.create_user_and_get_user_data()
        response = requests.post(ApiRoutes.LOGIN, data=user_data)
        assert response.status_code == HTTPStatus.OK

    @title('Проверка авторизации пользователя с неверным "email"')
    @description('Тест проверяет, что пользователь не может авторизоваться с неверным "email"')
    def test_login_user_with_incorrect_email(self):
        user_data = requests_api.create_user_and_get_user_data()
        incorrect_email = fake.email()
        password = user_data['password']
        incorrect_user_data = {
            'email': incorrect_email,
            'password': password
        }
        response = requests.post(ApiRoutes.LOGIN, data=incorrect_user_data)
        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert response.json()["message"] == USER_NOT_FOUND_MSG

    @title('Проверка авторизации пользователя с неверным паролем')
    @description('Тест проверяет, что пользователь не может авторизоваться с неверным паролем')
    def test_login_user_with_incorrect_password(self):
        user_data = requests_api.create_user_and_get_user_data()
        incorrect_password = generate_random_string()
        email = user_data['email']
        incorrect_user_data = {
            'email': email,
            'password': incorrect_password
        }
        response = requests.post(ApiRoutes.LOGIN, data=incorrect_user_data)
        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert response.json()["message"] == USER_NOT_FOUND_MSG
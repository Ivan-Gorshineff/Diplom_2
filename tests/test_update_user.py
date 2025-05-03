from http import HTTPStatus

from allure import description, title
import requests
from utils import requests_api
from utils.requests_api import ApiRoutes
from utils.data import *
from conftest import get_user_token
from utils.fakers import fake, generate_random_string


class TestUpdateUser:

    @title('Проверка изменения email авторизованного пользователя')
    @description('Тест проверяет, что авторизованный пользователь может изменить свой email')
    def test_update_user_update_email_with_login(self, get_user_token):
        token = get_user_token
        updated_email = fake.email()
        updated_user_data = {
            'email': updated_email
        }
        response = requests.patch(ApiRoutes.UPDATE_USER, headers={'Authorization': f'{token}'}, data=updated_user_data)
        assert response.status_code == HTTPStatus.OK

    @title('Проверка изменения пароля авторизованного пользователя')
    @description('Тест проверяет, что авторизованный пользователь может изменить свой пароль')
    def test_update_user_update_password_with_login(self, get_user_token):
        token = get_user_token
        updated_password = generate_random_string()
        updated_user_data = {
            'password': updated_password
        }
        response = requests.patch(ApiRoutes.UPDATE_USER, headers={'Authorization': f'{token}'}, data=updated_user_data)
        assert response.status_code == HTTPStatus.OK

    @title('Проверка изменения имени авторизованного пользователя')
    @description('Тест проверяет, что авторизованный пользователь может изменить свое имя')
    def test_update_user_update_name_with_login(self, get_user_token):
        token = get_user_token
        updated_name = fake.name()
        updates_user_data = {
            'name': updated_name
        }
        response = requests.patch(ApiRoutes.UPDATE_USER, headers={'Authorization': f'{token}'}, data=updates_user_data)
        assert response.status_code == HTTPStatus.OK

    @title('Проверка изменений данных пользователя без авторизации')
    @description('Тест проверяет, что неавторизованный пользователь не может изменить поля')
    def test_update_user_without_login(self):
        updated_name = fake.name()
        updated_email = fake.email()
        updated_password = generate_random_string()
        updated_user_data = {
            'name': updated_name,
            'email': updated_email,
            'password': updated_password
        }
        response = requests.patch(ApiRoutes.UPDATE_USER, data=updated_user_data)
        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert response.json()["message"] == USER_NOT_UPDATED_LOGIN_MSG

    @title('Проверка изменения почты пользователя на почту, которая используется')
    @description('Тест проверяет, что нельзя указать почку, котоая уже используется')
    def test_update_user_with_already_created_email(self, get_user_token):
        token = get_user_token
        user_data = requests_api.create_user_and_get_user_data()
        user_email = user_data['email']
        updated_email_already_exists = {
            'email': user_email
        }
        response = requests.patch(ApiRoutes.UPDATE_USER, headers={'Authorization': f'{token}'}, data=updated_email_already_exists)
        assert response.status_code == HTTPStatus.FORBIDDEN
        assert response.json()["message"] == USER_NOT_UPDATED_EMAIL_MSG



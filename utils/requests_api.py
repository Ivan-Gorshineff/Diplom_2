from allure import step
import requests
from utils.fakers import generate_user
from utils.routes import ApiRoutes


step('Регистрация нового пользователя и получение его данных')
def create_user_and_get_user_data():
    user_data = generate_user()
    response = requests.post(ApiRoutes.REGISTER, data=user_data)
    if response.status_code == 200:
        return user_data

step('Удаление пользователя по токену')
def delete_user(token: str):
    requests.delete(ApiRoutes.DELETE_USER, headers={'Authorization': f'{token}'})
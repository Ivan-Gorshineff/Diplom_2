import pytest
import requests
from utils import requests_api, data, fakers
from utils.routes import ApiRoutes


@pytest.fixture(scope='function')
def get_user_token():
    user_data = requests_api.create_user_and_get_user_data()
    email = user_data['email']
    password = user_data['password']
    name = user_data['name']
    payload = {
        'email': email,
        'password': password,
        'name': name
    }
    response = requests.post(ApiRoutes.LOGIN, data=payload)
    token = response.json().get('essToken')

    yield token
    requests_api.delete_user(token)
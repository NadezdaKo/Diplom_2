import pytest
import requests
from data import Data
from helpers import *

@pytest.fixture
def user():
    login_pass = register_new_user_and_return_login_password()
    yield login_pass
    if login_pass:
        response = login_user(login_pass[0], login_pass[1])
        if response.status_code == 200:
            user_id = response.json()["id"]
            delete_user(user_id)
            
@pytest.fixture
def order(ingredients):
    response = requests.post(Data.CREATE_ORDER, json=ingredients)
    number = response if response.status_code == 201 else None
    yield number
    
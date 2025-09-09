import pytest
import requests
import allure
from helpers import login_user, register_new_user_and_return_login_password
from data import Data

class TestCreateUser:
    @allure.title("Создание пользователя возвращает ok: true")
    def test_create_user_returns_ok_true(self):
        with allure.step('Создание пользоваателя'):
            login_pass = register_new_user_and_return_login_password()
            login_resp = login_user(login_pass[0], login_pass[1])
        assert login_resp.ok
        assert "accessToken" in login_resp.json()
        
    @allure.title("Нельзя создать двух одинаковых пользователей")
    def test_create_duplicate_user_fails(self):
        with allure.step('Создание пользователя'):
            login_pass = register_new_user_and_return_login_password()
            payload = {"email": login_pass[0], "password": login_pass[1], "name": login_pass[2]}
        with allure.step('Создание дубликата пользователя'):
            response = requests.post(Data.CREATE_USER, json=payload)
        assert response.status_code == 403
        assert "User already exists" == response.json().get('message')

    @pytest.mark.parametrize("payload", [{"email": "testuse@ya.ru","password":"12345678"}, {"name":"kekeke","password":"12345678"}])
    @allure.title("Создание пользователя без обязательных полей")
    def test_create_user_missing_fields_fails(self, payload):
        with allure.step('Создание пользователя'):
            response = requests.post(Data.CREATE_USER, data=payload)
        print(response.text)
        assert response.status_code == 403
        assert "Email, password and name are required fields" == response.json().get('message')
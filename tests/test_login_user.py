import requests
import allure
from helpers import register_new_user_and_return_login_password, login_user
from data import Data

class TestLoginUser:
    @allure.title("Авторизация пользователя: успех")
    def test_login_user_success(self):
        with allure.step('Создание пользователя'):
            login_pass = register_new_user_and_return_login_password()
        with allure.step('Авторизация пользователя'):
            response = requests.post(Data.LOGIN_USER, json={"email": login_pass[0], "password": login_pass[1]})
        assert response.ok == True
        assert "accessToken" in response.json()

    @allure.title("Авторизация с неверным логином и паролем")
    def test_login_wrong_credentials_fails(self):
        with allure.step('Создание пользователя'):
            login_pass = register_new_user_and_return_login_password()
        with allure.step('Попытка входа'):
            response = login_user(login_pass[0], "wrongpass")
        assert response.status_code == 401
        assert "email or password are incorrect" in response.json().get("message", "")
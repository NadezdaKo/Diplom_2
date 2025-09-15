import requests
import allure
from helpers import register_new_user_and_return_login_password
from data import Data

class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_login(self):
        with allure.step('Создание пользователя'):
            login_pass = register_new_user_and_return_login_password()
        with allure.step('Авторизация пользователя'):
            login_resp = requests.post(Data.LOGIN_USER, json={"email": login_pass[0], "password": login_pass[1]})
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
        headers = {"Authorization": login_resp.json().get('accessToken')}
        with allure.step('Попытка создания заказа с авторизацией'):
            response = requests.post(Data.CREATE_ORDER, json=payload, headers=headers)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_login(self):
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
        with allure.step('Попытка создания заказа без авторизации'):
            response = requests.post(Data.CREATE_ORDER, json=payload)
        assert response.status_code == 401
        assert response.json()["success"] is False

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self):
        with allure.step('Создание пользователя'):
            login_pass = register_new_user_and_return_login_password()
        with allure.step('Авторизация пользователя'):
            login_resp = requests.post(Data.LOGIN_USER, json={"email": login_pass[0], "password": login_pass[1]})
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
        headers = {"Authorization": login_resp.json().get('accessToken')}
        with allure.step('Попытка создания заказа с ингредиентами'):
            response = requests.post(Data.CREATE_ORDER, json=payload, headers=headers)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(login_user):
        with allure.step('Создание пользователя'):
            login_pass = register_new_user_and_return_login_password()
        with allure.step('Авторизация пользователя'):
            login_resp = requests.post(Data.LOGIN_USER, json={"email": login_pass[0], "password": login_pass[1]})
        payload = {"ingredients": []}
        headers = {"Authorization": login_resp.json().get('accessToken')}
        with allure.step('Попытка создания заказа без ингредиентов'):
            response = requests.post(Data.CREATE_ORDER, json=payload, headers=headers)
        assert response.status_code == 400
        assert response.json()["success"] is False

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredients(login_user):
        with allure.step('Создание пользователя'):
            login_pass = register_new_user_and_return_login_password()
        with allure.step('Авторизация пользователя'):
            login_resp = requests.post(Data.LOGIN_USER, json={"email": login_pass[0], "password": login_pass[1]})
        payload = {"ingredients": ['invalid_hash']}
        headers = {"Authorization": login_resp.json().get('accessToken')}
        with allure.step('Попытка создания заказа с неверным хешем'):
            response = requests.post(Data.CREATE_ORDER, json=payload, headers=headers)
        assert response.status_code == 400
        assert response.json()["success"] is False
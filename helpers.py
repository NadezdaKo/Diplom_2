import requests
import random
import string
import allure
from data import Data


@allure.step("Регистрация нового пользователя")
def register_new_user_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)+"@ya.ru"
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": login,
        "password": password,
        "name": name
    }

    response = requests.post(Data.CREATE_USER, data=payload)
    if response.ok:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(name)
        login_pass.append(response)

    return login_pass

@allure.step("Создание заказа")
def create_order():
    payload = {"ingredients": ["60d3b41abdacab0026a733c6","609646e4dc916e00276b2870"]}
    return requests.post(Data.CREATE_ORDER, json=payload)

@allure.step("Авторизация пользователя")
def login_user(login, password):
    payload = {"email": login, "password": password}
    return requests.post(Data.LOGIN_USER, json=payload)

@allure.step("Удаление пользователя")
def delete_user(user_id):
    return requests.delete(Data.DELETE_USER/{user_id})

@allure.step("Получение заказа по номеру")
def get_order_user_number(number):
    return requests.get(Data.GET_USER_ORDERS/{number})
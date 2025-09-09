BASE_URL = "https://stellarburgers.nomoreparties.site/"

class Data:
    CREATE_USER = f"{BASE_URL}/api/auth/register"
    LOGIN_USER = f"{BASE_URL}/api/auth/login"
    LOGOUT_USER = f"{BASE_URL}/api/auth/logout"
    TOKEN_USER = f"{BASE_URL}/api/auth/token"
    DATA_USER = f"{BASE_URL}/api/auth/user"
    DELETE_USER = f"{BASE_URL}/api/auth/user"
    CREATE_ORDER = f"{BASE_URL}/api/orders"
    GET_USER_ORDERS = f"{BASE_URL}/api/orders"

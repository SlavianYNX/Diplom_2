class UrlsApi:

    MAIN = ' https://stellarburgers.nomoreparties.site'
    CREATE_USER = MAIN + '/api/auth/register'
    LOGIN_USER = MAIN + '/api/auth/login'
    CREATE_ORDER = MAIN + '/api/orders'
    DELETE_USER = MAIN + '/api/auth/user'
    DATA_INGREDIENTS = MAIN + '/api/ingredients'


class Ingredient:

    data = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
    not_ingredient = {"ingredients": []}
    hash_bad = {"ingredients": ["61c0c5a71d1f82001bdaaa6", "61c0c5a71d1f82001bdaaa6"]}


class StatusCode:

    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    INTERNAL_SERVER_ERROR = 500

class TextResponse:

    CREATE_DOUBLE_USER = 'User already exists'
    SERVER_ERROR = 'Internal Server Error'
    NOT_INGREDIENTS = 'Ingredient ids must be provided'
    NOT_FIELD = 'Email, password and name are required fields'
    BAD_LOGIN_PASS = 'email or password are incorrect'
    TRUE = True
    FALSE = False
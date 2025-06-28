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

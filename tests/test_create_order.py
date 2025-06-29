import pytest
import allure
import requests
import data
from data import UrlsApi, Ingredient


class TestCreateOrder:

    @allure.title('Проверка создания заказа с авторизацией')
    def test_create_order_login(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': token}
        r = requests.post(UrlsApi.CREATE_ORDER, headers=headers, json=Ingredient.data)
        assert r.status_code == data.StatusCode.OK and r.json()["success"] == data.TextResponse.TRUE

    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order_not_login(self):
        r = requests.post(UrlsApi.CREATE_ORDER, data=Ingredient.data)
        assert r.status_code == data.StatusCode.OK and r.json()["success"] == data.TextResponse.TRUE

    @allure.title('Проверка создания заказа без ингредиента')
    def test_create_order_not_ingredient(self):
        r = requests.post(UrlsApi.CREATE_ORDER, data=Ingredient.not_ingredient)
        assert r.status_code == data.StatusCode.BAD_REQUEST and r.json()["success"] == data.TextResponse.FALSE
        assert r.json()["message"] == data.TextResponse.NOT_INGREDIENTS

    @allure.title('Проверка создания заказа с неверным хэшем ингредиента')
    def test_create_order_bad_hash(self):
        r = requests.post(UrlsApi.CREATE_ORDER, data=Ingredient.hash_bad)
        assert r.status_code == data.StatusCode.INTERNAL_SERVER_ERROR and data.TextResponse.SERVER_ERROR in r.text
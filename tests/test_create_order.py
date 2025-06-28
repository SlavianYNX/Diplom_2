import pytest
import allure
import requests
from data import UrlsApi, Ingredient
from conftest import create_new_user


class TestCreateOrder:

    @allure.title('Проверка создания заказа с авторизацией')
    def test_create_order_login(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': token}
        r = requests.post(UrlsApi.CREATE_ORDER, headers=headers, data=Ingredient.data)
        assert r.status_code == 200 and r.json()["success"] == True

    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order_not_login(self):
        r = requests.post(UrlsApi.CREATE_ORDER, data=Ingredient.data)
        assert r.status_code == 200 and r.json()["success"] == True

    @allure.title('Проверка создания заказа без ингредиента')
    def test_create_order_not_ingredient(self):
        r = requests.post(UrlsApi.CREATE_ORDER, data=Ingredient.not_ingredient)
        assert r.status_code == 400 and r.json()["success"] == False
        assert r.json()["message"] == "Ingredient ids must be provided"

    @allure.title('Проверка создания заказа с неверным хэшем ингредиента')
    def test_create_order_bad_hash(self):
        r = requests.post(UrlsApi.CREATE_ORDER, data=Ingredient.hash_bad)
        assert r.status_code == 500 and 'Internal Server Error' in r.text
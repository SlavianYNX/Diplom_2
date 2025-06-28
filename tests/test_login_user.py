import pytest
import allure
import requests
from data import UrlsApi
from helpers import UserData


class TestLoginUser:

    @allure.title('Проверка авторизации под существующим пользователем')
    def test_login_user(self):
        user = UserData.create_user_data()
        p = requests.post(UrlsApi.CREATE_USER, data=user)
        r = requests.post(UrlsApi.LOGIN_USER, data=user)
        assert r.status_code == 200 and r.json()["success"] == True

    @allure.title('Проверка авторизации с неверным логином и паролем')
    def test_login_no_user(self):
        user = UserData.create_user_no_name()
        r = requests.post(UrlsApi.LOGIN_USER, data=user)
        assert r.status_code ==401 and r.json()["message"] == "email or password are incorrect"
        assert r.json()["success"] == False
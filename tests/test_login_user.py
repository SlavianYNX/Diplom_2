import pytest
import allure
import requests
import data
from data import UrlsApi
from helpers import UserData


class TestLoginUser:

    @allure.title('Проверка авторизации под существующим пользователем')
    def test_login_user(self):
        user = UserData.create_user_data()
        p = requests.post(UrlsApi.CREATE_USER, data=user)
        r = requests.post(UrlsApi.LOGIN_USER, data=user)
        assert r.status_code == data.StatusCode.OK and r.json()["success"] == data.TextResponse.TRUE

    @allure.title('Проверка авторизации с неверным логином и паролем')
    def test_login_no_user(self):
        user = UserData.create_user_no_name()
        r = requests.post(UrlsApi.LOGIN_USER, data=user)
        assert r.status_code == data.StatusCode.UNAUTHORIZED and r.json()["message"] == data.TextResponse.BAD_LOGIN_PASS
        assert r.json()["success"] == data.TextResponse.FALSE
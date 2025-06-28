import pytest
import requests
import allure
from data import UrlsApi
from conftest import create_new_user
from helpers import UserData


class TestCreateUser:

    @allure.title('Проверка создания уникального пользователя')
    def test_create_user_ok(self, create_new_user):
        r = create_new_user
        assert r[1].status_code == 200 and r[1].json()["success"] == True

    @allure.title('Проверка создания пользователя, который уже зарегистрированный')
    def test_create_user_two_registered(self, create_new_user):
        response = create_new_user
        payload = response[0]
        r = requests.post(UrlsApi.CREATE_USER, data=payload)
        assert r.status_code == 403 and r.json()['message'] == "User already exists"

    @allure.title('Проверка создания пользователя и незаполнение одного из полей')
    @pytest.mark.parametrize('payload',(UserData.create_user_no_name(),
                                        UserData.create_user_no_password(),
                                        UserData.create_user_no_email()))
    def test_create_no_data(self, payload):
        r = requests.post(UrlsApi.CREATE_USER, data=payload)
        assert r.status_code == 403 and r.json()["message"] == "Email, password and name are required fields"
        assert r.json()["success"] == False
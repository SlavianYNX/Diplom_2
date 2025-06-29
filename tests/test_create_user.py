import pytest
import requests
import allure
import data
from data import UrlsApi
from helpers import UserData


class TestCreateUser:


    @allure.title('Проверка создания уникального пользователя')
    def test_create_user_ok(self, create_new_user):
        response = create_new_user
        assert response[1].status_code == data.StatusCode.OK and response[1].json()["success"] == data.TextResponse.TRUE

    @allure.title('Проверка создания пользователя, который уже зарегистрированный')
    def test_create_user_two_registered(self, create_new_user):
        response = create_new_user
        payload = response[0]
        r = requests.post(UrlsApi.CREATE_USER, json=payload)
        assert r.status_code == data.StatusCode.FORBIDDEN and r.json()['message'] == data.TextResponse.CREATE_DOUBLE_USER

    @allure.title('Проверка создания пользователя и незаполнение одного из полей')
    @pytest.mark.parametrize('payload',(UserData.create_user_no_name(),
                                        UserData.create_user_no_password(),
                                        UserData.create_user_no_email()))
    def test_create_no_data(self, payload):
        r = requests.post(UrlsApi.CREATE_USER, json=payload)
        assert r.status_code == data.StatusCode.FORBIDDEN and r.json()["message"] == data.TextResponse.NOT_FIELD
        assert r.json()["success"] == data.TextResponse.FALSE
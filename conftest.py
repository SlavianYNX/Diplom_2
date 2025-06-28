import pytest
import requests
from data import UrlsApi
from helpers import UserData


@pytest.fixture()
def create_new_user():
    payload = UserData.create_user_data()
    response = requests.post(UrlsApi.CREATE_USER, data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(UrlsApi.DELETE_USER, headers={'Authorization': token})


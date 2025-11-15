import pytest
import requests
from data import UrlsApi
from helpers import UserData


@pytest.fixture(autouse=True)
def create_new_user():
    payload = UserData.create_user_data()
    response = requests.post(UrlsApi.CREATE_USER, data=payload)
    token = response.json().get("accessToken", "")
    yield payload, response
    requests.delete(UrlsApi.DELETE_USER, headers={'Authorization': token})
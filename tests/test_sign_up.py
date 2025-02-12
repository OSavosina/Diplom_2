import allure
from constants import TestsMessages
from client.services import service_sign_up
from helpers.helpers import generate_fields_user
from data import TestsUserData


class TestCreateUser:
    @allure.title('Успешное создание юзера')
    def test_sign_up_success(self):
        fields_collection = generate_fields_user(TestsUserData.FULL_DICTIONARY_FIELDS)
        response = service_sign_up(fields_collection)

        assert response.status_code == 200


    @allure.title('Создание юзера с неполным набором полей')
    def test_sign_up_error(self):
        fields_collection = generate_fields_user(TestsUserData.LOGIN_AND_FIRSTNAME_FIELDS)
        response = service_sign_up(fields_collection)
        message = response.json()

        assert response.status_code == 403 and message['message'] == TestsMessages.CREATE_USER_ERROR


    @allure.title('Создание двух одинаковых юзеров')
    def test_sign_up_conflict(self):
        fields_collection = generate_fields_user(TestsUserData.FULL_DICTIONARY_FIELDS)
        service_sign_up(fields_collection)
        response = service_sign_up(fields_collection)
        message = response.json()

        assert response.status_code == 403 and message['message'] == TestsMessages.CREATE_USER_CONFLICT

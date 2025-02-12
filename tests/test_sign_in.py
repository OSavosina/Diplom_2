import allure
from constants import TestsMessages
from confest import fixture_create_user
from client.services import service_sign_in
from constants import UserProfileFields


class TestSignInUser:
    @allure.title('Успешная авторизация юзера')
    def test_sign_in_success(self, fixture_create_user):
        fields_collection = fixture_create_user
        response = service_sign_in({UserProfileFields.EMAIL: fields_collection[f'{UserProfileFields.EMAIL}'], UserProfileFields.PASSWORD: fields_collection[f'{UserProfileFields.PASSWORD}']})

        assert response.status_code == 200


    @allure.title('Авторизация с неполным набором полей')
    def test_login_user_error(self, fixture_create_user):
        fields_collection = fixture_create_user
        response = service_sign_in({UserProfileFields.EMAIL: fields_collection[f'{UserProfileFields.EMAIL}']})
        message = response.json()

        assert response.status_code == 401 and message['message'] == TestsMessages.LOGIN_USER_ERROR





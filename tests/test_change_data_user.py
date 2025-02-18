import allure
from confest import fixture_create_user
from client.services import service_sign_in, service_get_user_data, service_change_user_data
from constants import UserProfileFields, TestsMessages
from helpers.helpers import generate_fields_user
from data import TestsUserData


class TestChangeDataUser:
    @allure.title('Изменение данных авторизованного юзера')
    def test_change_data_user_authorise(self, fixture_create_user):
        prepare_data = fixture_create_user

        response_auth = service_sign_in({UserProfileFields.EMAIL: prepare_data[f'{UserProfileFields.EMAIL}'], UserProfileFields.PASSWORD: prepare_data[f'{UserProfileFields.PASSWORD}']})
        token = response_auth.json()['accessToken']

        generate_new_fields_for_service_change = generate_fields_user(TestsUserData.LOGIN_AND_FIRSTNAME_FIELDS)
        service_change_user_data(
            {
                UserProfileFields.EMAIL: generate_new_fields_for_service_change[f'{UserProfileFields.EMAIL}'],
                UserProfileFields.NAME: generate_new_fields_for_service_change[f'{UserProfileFields.NAME}']}
        ,
            {'auth_key': token}
        )


        response_user_data = service_get_user_data({'auth_key': token})
        message = response_user_data.json()

        assert (response_user_data.status_code == 200 and
                message['user']['email'] == generate_new_fields_for_service_change[f'{UserProfileFields.EMAIL}'] and
                message['user']['name'] == generate_new_fields_for_service_change[f'{UserProfileFields.NAME}'])



    @allure.title('Изменение данных неавторизованного юзера')
    def test_change_data_user_no_authorise(self, fixture_create_user):
        generate_new_fields_for_service_change = generate_fields_user(TestsUserData.LOGIN_AND_FIRSTNAME_FIELDS)
        response_user_data = service_change_user_data(
            {
                UserProfileFields.EMAIL: generate_new_fields_for_service_change[f'{UserProfileFields.EMAIL}'],
                UserProfileFields.NAME: generate_new_fields_for_service_change[f'{UserProfileFields.NAME}']},
            {'auth_key': ''}

        )

        message = response_user_data.json()

        assert response_user_data.status_code == 401 and message['message'] == TestsMessages.NO_AUTHORISE_USER
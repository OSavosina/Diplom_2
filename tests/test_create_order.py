import allure
from confest import fixture_create_user
from client.services import service_create_order, service_get_ingredients, service_sign_in
from constants import UserProfileFields, TestsMessages


class TestCreateOrder:
    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_authorise_success(self, fixture_create_user):
        prepare_data = fixture_create_user

        response_auth = service_sign_in({UserProfileFields.EMAIL: prepare_data[f'{UserProfileFields.EMAIL}'],UserProfileFields.PASSWORD: prepare_data[f'{UserProfileFields.PASSWORD}']})
        token = response_auth.json()['accessToken']

        response_ingredients = service_get_ingredients()
        ingredient = response_ingredients.json()['data'][0]['_id']

        response = service_create_order({'ingredients': [ingredient]}, {'auth_key': token})
        message = response.json()

        assert response.status_code == 200 and message['order']['owner']


    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_authorise(self):
        response_ingredients = service_get_ingredients()
        ingredient = response_ingredients.json()['data'][0]['_id']

        response = service_create_order({'ingredients': [ingredient]}, {'auth_key': ''})
        message = response.json()

        assert response.status_code == 200 and message['order']['owner']


    @allure.title('Создание заказа без ингредиента')
    def test_create_order_without_ingredient(self, fixture_create_user):
        prepare_data = fixture_create_user

        response_auth = service_sign_in({UserProfileFields.EMAIL: prepare_data[f'{UserProfileFields.EMAIL}'],
                                         UserProfileFields.PASSWORD: prepare_data[f'{UserProfileFields.PASSWORD}']})
        token = response_auth.json()['accessToken']

        response = service_create_order({'ingredients': []}, {'auth_key': token})
        message = response.json()

        assert response.status_code == 400 and message['message'] == TestsMessages.NOT_INGREDIENT


    @allure.title('Создание заказа с невалидным хешем ингредиента')
    def test_create_order_hash_error_ingredient(self, fixture_create_user):
        prepare_data = fixture_create_user

        response_auth = service_sign_in({UserProfileFields.EMAIL: prepare_data[f'{UserProfileFields.EMAIL}'],
                                         UserProfileFields.PASSWORD: prepare_data[f'{UserProfileFields.PASSWORD}']})
        token = response_auth.json()['accessToken']

        response = service_create_order({'ingredients': ['22333']}, {'auth_key': token})

        assert response.status_code == 500
import allure
from confest import fixture_create_user
from client.services import service_create_order, service_sign_in, service_get_ingredients, service_get_orders_list
from constants import UserProfileFields, TestsMessages


class TestGetUserSOrder:
    @allure.title('Получение заказов авторизованного юзера')
    def test_get_users_order_with_authorise_success(self, fixture_create_user):
        prepare_data = fixture_create_user

        response_auth = service_sign_in({UserProfileFields.EMAIL: prepare_data[f'{UserProfileFields.EMAIL}'],
                                         UserProfileFields.PASSWORD: prepare_data[f'{UserProfileFields.PASSWORD}']})
        token = response_auth.json()['accessToken']

        response_ingredients = service_get_ingredients()
        ingredient = response_ingredients.json()['data'][0]['_id']

        service_create_order({'ingredients': [ingredient]}, {'auth_key': token})

        response = service_get_orders_list({'auth_key': token})
        message = response.json()

        assert response.status_code == 200 and len(message['orders']) != 0


    @allure.title('Получение заказов неавторизованного юзера')
    def test_get_users_order_with_user_no_authorise(self):

        response_ingredients = service_get_ingredients()
        ingredient = response_ingredients.json()['data'][0]['_id']

        service_create_order({'ingredients': [ingredient]}, {'auth_key': ''})

        response = service_get_orders_list({'auth_key': ''})
        message = response.json()

        assert response.status_code == 401 and message['message'] == TestsMessages.NO_AUTHORISE_USER

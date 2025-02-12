from client.api import post_api, get_api, patch_api, delete_api
from constants import RoutesName
import allure


@allure.step('Создание юзера')
def service_sign_up(data):
    return post_api(RoutesName.SIGN_UP_USER, data)

@allure.step('Удаление юзера')
def service_delete_user():
    return delete_api(RoutesName.DELETE_USER)

@allure.step('Авторизация юзера')
def service_sign_in(data):
    return post_api(RoutesName.SIGN_IN_USER, data)

@allure.step('Логаут')
def service_logout(data):
    return post_api(RoutesName.LOGOUT, data)

@allure.step('Запрос данных юзера')
def service_get_user_data(headers_dict):
    prepare_headers = {'Authorization': headers_dict['auth_key']}
    return get_api(RoutesName.GET_USER_DATA, prepare_headers)

@allure.step('Обновление данных юзера')
def service_change_user_data(data, headers_dict):
    prepare_headers = {'Authorization': headers_dict['auth_key']}
    return patch_api(RoutesName.GET_USER_DATA, data, prepare_headers)

@allure.step('Создание заказа')
def service_create_order(data, headers_dict):
    prepare_headers = {'Authorization': headers_dict['auth_key']}
    return post_api(RoutesName.CREATE_ORDER, data, prepare_headers)

@allure.step('Получение списка ингредиентов')
def service_get_ingredients():
    return get_api(RoutesName.INGREDIENTS)

@allure.step('Получение заказов пользователя')
def service_get_orders_list(headers_dict):
    prepare_headers = {'Authorization': headers_dict['auth_key']}
    return get_api(RoutesName.CREATE_ORDER, prepare_headers)
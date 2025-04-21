class HostName:
    HOST_NAME = 'https://stellarburgers.nomoreparties.site/api'

class RoutesName:
    SIGN_UP_USER = '/auth/register'
    SIGN_IN_USER = '/auth/login'
    GET_USER_DATA = '/auth/user'
    DELETE_USER = '/auth/user'
    LOGOUT = '/auth/logout'
    CREATE_ORDER = '/orders'
    INGREDIENTS = '/ingredients'

class UserProfileFields:
    EMAIL = 'email'
    PASSWORD = 'password'
    NAME = 'name'

class TestsMessages:
    CREATE_USER_ERROR = "Email, password and name are required fields"
    CREATE_USER_CONFLICT = "User already exists"
    LOGIN_USER_ERROR = 'email or password are incorrect'
    NO_AUTHORISE_USER = 'You should be authorised'
    ADD_EXIST_EMAIL = 'User with such email already exists'
    NOT_INGREDIENT = 'Ingredient ids must be provided'





import pytest
from helpers.helpers import generate_fields_user
from client.services import service_sign_up, service_delete_user
from data import TestsUserData


@pytest.fixture
def fixture_create_user():
    prepare_data = generate_fields_user(TestsUserData.FULL_DICTIONARY_FIELDS)
    service_sign_up(prepare_data)
    yield prepare_data
    service_delete_user()


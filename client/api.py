import requests
from constants import HostName


def post_api(path='', data=None, headers=None):
    return requests.post(f'{HostName.HOST_NAME}{path}', data=data, headers=headers)

def get_api(path='', headers=None):
    return requests.get(f'{HostName.HOST_NAME}{path}', headers=headers)

def delete_api(path=''):
    return requests.delete(f'{HostName.HOST_NAME}{path}')

def patch_api(path='', data=None, headers=None):
    return requests.patch(f'{HostName.HOST_NAME}{path}', data=data, headers=headers)
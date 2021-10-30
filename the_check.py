import requests
from settings import API_KEY, BASE_URL


def initial_commit(name):
    print(f'Initial commit, {name}')


def get_check(api_key, base_url, fn, fd, fp, t, n, s):
    request_url = base_url + '/?'
    api_request = requests.post(request_url).json()
    pass


if __name__ == '__main__':
    initial_commit('The Check')

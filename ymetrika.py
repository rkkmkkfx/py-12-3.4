import requests
from urllib.parse import urlencode
from pprint import pprint

APP_ID = '3015b80010a2428eac510219c327b87c'
AUTH_URL = 'https://oauth.yandex.ru/authorize'

oauth_data = {
    'response_type': 'token',
    'client_id': APP_ID
}
print('?'.join((AUTH_URL, urlencode(oauth_data))))

TOKEN = 'AQAAAAAMG-OlAATTp7ub0BuADkr_rq0OCS6M7gI'
COUNTER_ID = 47797873


class YaMetrikaUser:

    API_URL = 'https://api-metrika.yandex.ru/stat/v1/data'

    def __init__(self, token, counter_id):
        self.token = token
        self.counter_id = counter_id
        self.headers = {
            'Authorization': 'OAuth {}'.format(self.token),
            'Content-Type': 'application/json'
        }

    @property
    def visits(self):
        params = {
            'metrics': 'ym:s:visits',
            'id': self.counter_id
        }
        return requests.get(self.API_URL, params, headers=self.headers).json()

    @property
    def pageviews(self):
        params = {
            'metrics': 'ym:s:pageviews',
            'id': self.counter_id
        }
        return requests.get(self.API_URL, params, headers=self.headers).json()

    @property
    def users(self):
        params = {
            'metrics': 'ym:s:users',
            'id': self.counter_id
        }
        return requests.get(self.API_URL, params, headers=self.headers).json()


ymetric_user = YaMetrikaUser(TOKEN, COUNTER_ID)
pprint(ymetric_user.visits)
pprint(ymetric_user.pageviews)
pprint(ymetric_user.users)

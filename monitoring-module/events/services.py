# https
import json
import requests


class Authentication():
    def __init__(self):
        self.token = 'am9obmRvZTpBM2RkajN3'
        self.api_url_base = 'https://127.0.0.1:8080/auth/access_token'

    def get_access_token(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Authorization': 'Basic {0}'.format(self.token)}
        payload = {'grant_type': 'password',
                   'username': 'johndoe',
                   'password': 'A3ddj3w'}
        response = requests.post(self.api_url_base, verify=False,
                                 headers=headers, data=payload)
        print(response)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None


class Events():
    def send_event(event):
        auth = Authentication()
        api_token = auth.get_access_token()
        api_url_base = 'https://127.0.0.1:8080/v1/monitoring/events'
        # api_url_base = 'http://127.0.0.1:3000/monitoring/events'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(api_token['token']['accessToken'])}
        api_url = '{0}'.format(api_url_base)
        response = requests.post(api_url, verify=False,
                                 headers=headers, json=event)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

import requests
from requests import Response

from qbit_py_sdk.dto import CodeOutput, RefreshTokenOutput
from qbit_py_sdk.dto.access_token_output import AccessTokenOutput
from qbit_py_sdk.qbit_response import QbitResponse


class QbitClient(object):
    BASE_URL = "https://api-global.qbitnetwork.com"
    ACCESS_TOKEN = ""

    def __init__(self, app_id: str = None, app_secret: str = None, base_url: str = BASE_URL):
        self.BASE_URL = base_url
        self.app_id = app_id
        self.app_secret = app_secret

    # 获取code
    def get_code(self, state: str = "", redirect_uri: str = "") -> CodeOutput:
        url: str = self.BASE_URL + "/open-api/oauth/authorize"
        params = {
            "clientId": self.app_id,
            "state": state,
            "redirectUri": redirect_uri
        }

        headers = {
            'Content-Type': 'application/json',
        }

        response: Response = requests.get(url=url, params=params, headers=headers)
        res = response.json()
        status = response.status_code
        if 200 <= status < 300:
            return CodeOutput.parse(res)
        else:
            raise Exception(res.get("message", "error"))

    # 获取access token
    def get_access_token(self, code: str) -> AccessTokenOutput:
        url: str = self.BASE_URL + "/open-api/oauth/access-token"
        params = {
            "clientId": self.app_id,
            "clientSecret": self.app_secret,
            "code": code
        }

        headers = {
            'Content-Type': 'application/json',
        }
        response: Response = requests.post(url=url, headers=headers, json=params)
        return AccessTokenOutput.parse(response.json())

    # 刷新access token
    def refresh_access_token(self, refresh_token: str) -> RefreshTokenOutput:
        url: str = self.BASE_URL + "/open-api/oauth/refresh-token"
        params = {
            "clientId": self.app_id,
            "refreshToken": refresh_token
        }

        headers = {
            'Content-Type': 'application/json',
        }
        response: Response = requests.post(url=url, headers=headers, json=params)
        return RefreshTokenOutput.parse(response.json())

    # 设置 access_token
    def config(self, access_token: str):
        self.ACCESS_TOKEN = access_token
        return self

    # get 请求
    def get_request(self, url: str, **params) -> QbitResponse:
        headers = {
            'x-qbit-access-token': self.ACCESS_TOKEN,
            'Content-Type': 'application/json',
        }
        response: Response = requests.get(url=url, params=params, headers=headers)
        return QbitResponse.parse(response)

    # delete 请求
    def delete_request(self, url: str, **json) -> QbitResponse:
        headers = {
            'x-qbit-access-token': self.ACCESS_TOKEN,
            'Content-Type': 'application/json',
        }
        response: Response = requests.delete(url, json=json, headers=headers)
        return QbitResponse.parse(response)

    # put 请求
    def put_request(self, url: str, **json) -> QbitResponse:
        headers = {
            'x-qbit-access-token': self.ACCESS_TOKEN,
            'Content-Type': 'application/json',
        }
        response: Response = requests.put(url, json=json, headers=headers)
        return QbitResponse.parse(response)

    # post 请求
    def post_request(self, url: str, **json) -> QbitResponse:
        headers = {
            'x-qbit-access-token': self.ACCESS_TOKEN,
            'Content-Type': 'application/json',
        }
        response: Response = requests.post(url, json=json, headers=headers)
        return QbitResponse.parse(response)

"""
获取access token
"""


class AccessTokenOutput:
    def __init__(self, code: int, message: str, access_token: str, refresh_token: str, expires_in: int, timestamp: str):
        self._code = code
        self._message = message
        self._access_token = access_token
        self._refresh_token = refresh_token
        self._expires_in = expires_in
        self._timestamp = timestamp

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    @property
    def accessToken(self):
        return self._access_token

    @accessToken.setter
    def accessToken(self, access_token):
        self._access_token = access_token

    @property
    def refreshToken(self):
        return self._refresh_token

    @refreshToken.setter
    def refreshToken(self, refresh_token):
        self._refresh_token = refresh_token

    @property
    def expiresIn(self):
        return self._expires_in

    @expiresIn.setter
    def expiresIn(self, expires_in):
        self._expires_in = expires_in

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        self._timestamp = timestamp

    def __str__(self) -> str:
        return f"AccessTokenOutput[code={self.code} message={self.message} accessToken={self.accessToken} " \
               f"refreshToken={self.refreshToken} expiresIn={self.expiresIn} timestamp={self.timestamp}] "

    @staticmethod
    def parse(content: dict):
        return AccessTokenOutput(content.get("code", 0), content.get("message", 'ok'),
                                 content.get("accessToken", None), content.get("refreshToken", None),
                                 content.get("expiresIn", None), content.get("timestamp", None))

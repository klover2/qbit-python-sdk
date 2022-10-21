from requests import Response

from qbit_py_sdk.qbit_response_content import QbitResponseContent


# 返回内容
class QbitResponse:
    def __init__(self, status: int, reason: str, content: QbitResponseContent = None):
        self._status = status
        self._reason = reason
        self._content = content

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, reason):
        self._reason = reason

    @property
    def content(self) -> QbitResponseContent:
        return self._content

    @content.setter
    def content(self, content: QbitResponseContent):
        self._content = content

    def __str__(self) -> str:
        return f"FeishuResponse[status={self.status} reason={self.reason} content={self.content}]"

    @staticmethod
    def parse(res: Response):
        return QbitResponse(res.status_code, res.reason, QbitResponseContent.parse(res.json()))

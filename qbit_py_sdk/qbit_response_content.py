from typing import Any

CODE, MESSAGE, DATA = "code", "message", "data"


# 返回内容
class QbitResponseContent:
    def __init__(self, code: int, message: str, data: Any = None):
        self._code = code
        self._message = message
        self._data = data

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
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def __str__(self) -> str:
        return f"QbitResponseContent[code={self.code} message={self.message} data={self.data}]"

    @staticmethod
    def parse(content: dict):
        return QbitResponseContent(content.get(CODE, -1), content.get(MESSAGE, 'error'), content.get(DATA, None))

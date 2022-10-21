"""
获取code
"""


class CodeOutput:
    def __init__(self, timestamp: int, code: str, state: str):
        self._timestamp = timestamp
        self._code = code
        self._state = state

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        self._timestamp = timestamp

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    def __str__(self) -> str:
        return f"CodeOutput[timestamp={self.timestamp} code={self.code} state={self.state}]"

    @staticmethod
    def parse(content: dict):
        return CodeOutput(content.get("timestamp", None), content.get("code", None), content.get("state", None))

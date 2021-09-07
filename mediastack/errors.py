from typing import Dict
from typing import List


class MediastackApiError(Exception):

    def __init__(self, code: str, message: str, context: Dict[str, List[str]] = {}) -> None:
        self.code = code
        self.message = message
        self.context = context

    def __str__(self) -> str:
        return f"code: {self.code}; message: {self.message}, context: {self.context}"

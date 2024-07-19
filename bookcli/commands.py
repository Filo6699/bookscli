from typing import Callable, List


class Command:
    def __init__(self, keyword: str, func: Callable) -> None:
        self.keyword: str = keyword
        self._func = func

    def execute(self, args: List[str]):
        self._func(args)

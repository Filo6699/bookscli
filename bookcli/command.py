from typing import Callable, List, Optional


class Command:
    def __init__(
        self,
        keyword: str,
        func: Callable,
        description: Optional[str] = None,
    ) -> None:
        self.keyword: str = keyword
        self.description: Optional[str] = description
        self._func = func

    def execute(self):
        self._func()

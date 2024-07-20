from typing import Optional, List

from bookcli.command import Command


commands: List[Command] = []


def register_command(keyword: str, description: Optional[str]):
    """Декоратор для загрузки команды в CLI."""

    def wrapper(func):
        commands.append(Command(keyword, func, description))

    return wrapper


# Инициализация модулей с командами
import bookcli.commands.books
import bookcli.commands.storage

import importlib.util
from typing import List
from pathlib import Path

from bookcli.utils import Format
from bookcli.command import Command
from bookcli.books import Library
from bookcli.commands import commands


def print_help(commands: List[Command]) -> None:
    """Выводит меню помощи. Генерируется по входным командам и их данным."""

    # Hard-coded команды, не являются модулями
    phantom_commands: List[Command] = [
        Command("help", lambda: None, "Prints this message"),
        Command("exit", lambda: None, "Exit the CLI"),
    ]
    all_cmds = commands + phantom_commands

    print(f"\n{Format.REVERSE} Help menu {Format.RESET}")
    print(f"Bookcli is a tool for managing book libraries.\n")
    print(f"{Format.REVERSE} Commands {Format.RESET}")

    for cmd in all_cmds:
        suffix = f" - {cmd.description}" if cmd.description != None else ""
        print(f"- {Format.UNDERLINE}{cmd.keyword}{Format.RESET}{suffix}")
    print()


def main_loop():
    """Основной цикл программы. Подгружает и хэнделит все команды, принимает ввод."""
    print_help(commands)
    running = True
    while running:
        try:
            command = input("> ").strip()
        except KeyboardInterrupt:
            running = False
            continue

        if command == "":
            continue

        parts = command.split(" ")
        keyword = parts[0]

        if keyword == "exit":
            running = False
            continue

        if keyword == "help":
            print_help(commands)
            continue

        for cmd in commands:
            if cmd.keyword == keyword:
                cmd.execute()
                print()  # дополнительный пробел
                break
        else:  # Если ни одна команда не выполнена
            print(
                f"{Format.RED}{Format.REVERSE} Unknown command. Use `help` for additional information {Format.RESET}"
            )

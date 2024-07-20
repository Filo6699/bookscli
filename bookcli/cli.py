import importlib.util
from typing import List
from pathlib import Path

from bookcli.utils import Format
from bookcli.commands import Command
from bookcli.books import Library


def load_commands() -> List[Command]:
    """Загружает все команды из папки commands/ и возвращает их списком.

    Ищет переменную COMMANDS в каждом файле. Эта переменная должна быть типа List[Command].
    """
    commands = []
    commands_folder = Path(__file__).parent / "commands"

    for file in commands_folder.glob("*.py"):
        try:
            spec = importlib.util.spec_from_file_location(file.stem, file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, "COMMANDS"):
                commands.extend(getattr(module, "COMMANDS"))
            else:
                print(f"Module {file.stem} does not have variable COMMANDS")
        except Exception as e:
            print(f"Failed to load {file.stem}: {e}")

    return commands


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
        suffix = " - " if cmd.description != None else ""
        print(
            f"- {Format.UNDERLINE}{cmd.keyword}{Format.RESET}{suffix}{cmd.description}"
        )
    print()


def main_loop():
    commands = load_commands()

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
        args = parts[1:]

        if keyword == "exit":
            running = False
            continue

        if keyword == "help":
            print_help(commands)
            continue

        for cmd in commands:
            if cmd.keyword == keyword:
                cmd.execute(args)
                break
        else:  # Если ни одна команда не выполнена
            print("Unknown command. Use `help` for additional information.")

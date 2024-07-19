import importlib.util
from typing import List
from pathlib import Path

from bookcli.commands import Command


def load_commands() -> List[Command]:
    """Загружает все команды из папки commands/ и возвращает их списком."""
    commands = []
    commands_folder = Path(__file__).parent / "commands"
    target_variable = "COMMANDS"  # Извлекаемая переменная

    for file in commands_folder.glob("*.py"):
        try:
            spec = importlib.util.spec_from_file_location(file.stem, file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, target_variable):
                commands.extend(getattr(module, target_variable))
            else:
                print(f"Module {file.stem} does not have variable {target_variable}")
        except Exception as e:
            print(f"Failed to load {file.stem}: {e}")

    return commands


def main_loop():
    commands = load_commands()
    print(commands)

    print("Use `help` to view a guide.")
    running = True
    while running:
        command = input("> ").strip()

        if command == "":
            continue

        parts = command.split(" ")
        keyword = parts[0]
        args = parts[1:]

        if keyword == "quit":
            running = False
            continue

        for cmd in commands:
            if cmd.keyword == keyword:
                cmd.execute(args)
                break
        else:  # Если ни одна команда не выполнена
            print("Unknown command. Use `help` for additional information.")

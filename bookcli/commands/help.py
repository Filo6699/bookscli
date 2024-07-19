from typing import List

from bookcli.commands import Command


help_msg = """
help me
"""


def help_cmd(args: List[str] = None):
    print(help_msg)


COMMANDS: List[Command] = [
    Command("help", help_cmd),
]

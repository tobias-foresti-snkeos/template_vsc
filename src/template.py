"""----------------------------------------------------------------------------
    Template script created by Tobias Foresti MAIN
    ---------------------------------------------------------------------------
"""

import argparse
import os


class CmdColors:
    """strings to color the command prompt output"""

    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"


def get_input_args():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument("-i", "--input", metavar="string", action="store", type=str, required=True, help="string to print to prompt")
    my_parser.add_argument("-d", "--dashes", action="store_true", help="prettify output with dashes")
    my_parser.add_argument("-s", "--stars", action="store_true", help="prettify output with stars")

    args = my_parser.parse_args()
    return args.input, args.dashes, args.stars


def print_message_to_prompt(input_message, dashes=None, stars=None):
    """prints message to the command line prompt

    Args:
        input_message (string): message to print to the command line
        dashes (bool, optional): add dashes to prompt. Defaults to None.
        stars (bool, optional): add stars to prompt. Defaults to None.
    """
    if not input_message:
        raise ValueError(f"{CmdColors.FAIL}ERROR: you need an input!{CmdColors.ENDC}")
    os.system("")
    if dashes:
        print(f"{CmdColors.WARNING}{'-'*42}\n{CmdColors.ENDC}")
    if stars:
        print(f"{CmdColors.FAIL}{'*'*42}\n{CmdColors.ENDC}")
    print(input_message)
    if dashes:
        print(f"{CmdColors.WARNING}{'-'*42}\n{CmdColors.ENDC}")
    if stars:
        print(f"{CmdColors.FAIL}{'*'*42}\n{CmdColors.ENDC}")


if __name__ == "__main__":
    try:
        print_message_to_prompt(*get_input_args())
    except ValueError as value_error:
        print(value_error)

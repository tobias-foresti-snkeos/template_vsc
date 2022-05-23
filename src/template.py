"""----------------------------------------------------------------------------
    Template script created by Tobias Foresti
    ---------------------------------------------------------------------------
"""

import argparse


class CmdColors:
    """strings to color the command prompt output"""

    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"


def get_input_args():
    """get the input arguments from commandline

    Returns:
        tuple: containing the input arguments
    """
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument(
        "-i",
        "--input",
        metavar="string",
        action="store",
        type=str,
        required=True,
        help="string to print to prompt",
    )
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
    if dashes:
        print(f"{'-'*42}\n")
    if stars:
        print(f"{'*'*42}\n")
    print(input_message)
    if dashes:
        print(f"\n{'-'*42}")
    if stars:
        print(f"\n{'*'*42}")


if __name__ == "__main__":
    try:
        print_message_to_prompt(*get_input_args())
    except ValueError as value_error:
        print(value_error)

"""simple test file to test the functionality of the template.py file.
"""

import pytest
from template import print_message_to_prompt


def test_print_message_to_prompt(capfd):
    """test the function print_message_to_prompt

    Args:
        capfd (any): object given by pytest to test the output of the console
    """
    print_message_to_prompt("test message")
    # pylint: disable=unused-variable
    out, err = capfd.readouterr()
    assert out == "test message\n"

    with pytest.raises(ValueError):
        print_message_to_prompt(None)

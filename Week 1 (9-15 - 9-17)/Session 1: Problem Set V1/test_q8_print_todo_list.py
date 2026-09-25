# Edge case: an empty list should still print the header, but no numbered items.

import io
from contextlib import redirect_stdout

from q8_print_todo_list import print_todo_list


def test_print_todo_list_regular():
    tasks = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        print_todo_list(tasks)
    output = buffer.getvalue().strip().splitlines()
    assert output[0] == "Pooh's To Dos:"
    assert output[1] == "1. Count all the bees in the hive"
    assert output[2] == "2. Chase all the clouds from the sky"
    assert output[3] == "3. Think"
    assert output[4] == "4. Stoutness Exercises"


def test_print_todo_list_empty():
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        print_todo_list([])
    assert buffer.getvalue().strip() == "Pooh's To Dos:"

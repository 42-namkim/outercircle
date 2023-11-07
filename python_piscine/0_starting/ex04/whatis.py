#AssertionError! assert condition, msg

import sys

args = sys.argv
try:
    assert len(args) <= 2, "more than one argument is provided"
    if len(args) != 1:
        try:
            num = int(args[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        if num % 2:
            print("I'm Odd.")
        else:
            print("I'm Even.")
except AssertionError as error:
    print("AssertionError: ", end = '')
    print(error)
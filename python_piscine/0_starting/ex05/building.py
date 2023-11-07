import sys
import string


def count(object: str) -> dict:
    """this function is to count each character in the argument string"""
    res = {
        "chars": len(object),
        "uppers": 0,
        "lowers": 0,
        "p_marks": 0,
        "spaces": 0,
        "digits": 0
    }
    for s in object:
        if s.isupper():
            res["uppers"] += 1
        elif s.islower():
            res["lowers"] += 1
        elif s.isspace():
            res["spaces"] += 1
        elif s.isdigit():
            res["digits"] += 1
        elif s in string.punctuation:
            res["p_marks"] += 1
    return res


def print_count(res: dict):
    """this function is to print the result of the function above"""
    print(
            f'The text contains {res["chars"]} characters: \n'
            f'{res["uppers"]} upper letters \n'
            f'{res["lowers"]} lower letters \n'
            f'{res["p_marks"]} punctuation marks \n'
            f'{res["spaces"]} spaces \n'
            f'{res["digits"]} digits'
        )


def get_args():
    args = sys.argv[1:]
    if len(args) == 0:  # or args[0] == None:
        print("What is the text to count?")
        args.append(sys.stdin.readline())
    assert len(args) < 2, "more than 1 argument is provided"
    return (args)


def main():
    try:
        args = get_args()
        res = count(args[0])
        print_count(res)
    except AssertionError as error:
        print(f'AssertionError: {error}')


# run if only the module is not imported but is run on the interpreter
if __name__ == "__main__":
    main()

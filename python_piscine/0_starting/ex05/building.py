import sys
import string


def count(object: str) -> dict:
    print(type(object))
    """this function is to count each character in the argument string"""
    res = {
        "chars": 0,
        "uppers": 0,
        "lowers": 0,
        "p_marks": 0,
        "spaces": 0,
        "digits": 0
    }
    for s in str:
        if s.isupper():
            res["uppers"] + 1
        elif s.islower():
            res["lowers"] + 1
        elif s in string.punctuation:
            res["p_marks"] + 1
        elif s in string.whitespace:
            res["spaces"] + 1
        elif s in string.digits:
            res["digits"] + 1
    res["chars"] = sum(value for _, value in res())
    return res


def print_count(res: dict):
    """this function is to print the result of the function above"""
    print(
            f'The text contains {res["chars"]} characters:'
            f'{res["uppers"]} upper letters'
            f'{res["lowers"]} lower letters'
            f'{res["p_marks"]} punctuation marks'
            f'{res["spaces"]} spaces'
            f'{res["digits"]} digits'
        )


def main():
    try:
        args = sys.argv[1:]
        assert len(args) > 0, "should provide 1 argument"
        assert len(args) < 2, "more than 1 argument is provided"
        print_count(count(str(args[0])))

    except AssertionError as error:
        print(f'AssertionError: {error}')


# run if only the module is not imported but is run on the interpreter
if __name__ == "__main__":
    main()

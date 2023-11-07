import sys
import string


def count(object: str) -> dict:
    """this function is to count each character in the argument string"""
    print(object)
    res = {
        "chars": 0,
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
        elif s in string.punctuation:
            res["p_marks"] += 1
        elif s in string.whitespace:
            res["spaces"] += 1
        elif s in string.digits:
            res["digits"] += 1
    res["chars"] = sum(res.values())
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


def main():
    try:
        args = sys.argv[1:]
        if len(args) == 0:
            ft_input = ''
            try:
                while True:
                    ft_input += input()
            except EOFError:
                args.append(ft_input)
        assert len(args) < 2, "more than 1 argument is provided"
        print_count(count(str(args[0])))

    except AssertionError as error:
        print(f'AssertionError: {error}')


# run if only the module is not imported but is run on the interpreter
if __name__ == "__main__":
    main()

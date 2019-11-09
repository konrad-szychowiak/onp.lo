def _oper(token):
    return f"\033[1m{token}\033[0m"


def _not(token):
    return f"\033[1;31m{token}\033[0m"


def _quantifier(token):
    return f"\033[35m{token}\033[0m"


def _func(token):
    return f"\033[34m{token}\033[0m"


_quantifiers = ['FORALL', '∀', 'EXISTS', '∃']
_1args = ['NOT', '~', '¬']
_2args = ['AND', '&', '∧', 'OR', '|', '∨',
          'IMPLIES', '→', 'IFF', '↔', 'XOR', '⊕']

formula = []


def init(form: list):
    formula = form

    try:
        answer = analyse(formula)
    except IndexError:
        return _not("[!] To few elements in given form")

    if len(answer.split()) != 1 and len(answer.split()) != len(answer.split(', ')):
        return f"({answer})"

    else:
        return answer


def analyse(arr: list):
    """
    Funcion processes and prints tokens from imput
    with corresponding types.
    """

    # print(arr)
    if len(arr) == 1:
        last = arr[0]
        arr.pop()
        return last

    else:
        token = arr.pop()

        if token in _quantifiers:
            formula = analyse(arr)
            variable = analyse(arr)
            return f"{_quantifier(token)} {variable} ({formula})"

        elif token in _1args:
            arg_1 = analyse(arr)
            return f"{_not(token)} {arg_1}"

        elif token in _2args:
            arg_2 = analyse(arr)
            arg_1 = analyse(arr)
            return f"({arg_1}) {_oper(token)} ({arg_2})"

        elif token.find('/') != -1:
            token = token.split('/')
            tmp_string = ""

            for arg in range(int(token.pop())):
                arg = analyse(arr)
                tmp_string = f"{arg}, " + tmp_string

            tmp_string = tmp_string[:-2]
            return f"{_func(token[0])}({tmp_string})"

        else:
            return f"{token}"


def end(pre=False):
    if pre:
        print("")
    print("| \033[1;30mEND\033[0m")

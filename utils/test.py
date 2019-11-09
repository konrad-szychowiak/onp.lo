_quantifiers = ['FORALL', '∀', 'EXISTS', '∃']
_1args = ['NOT', '~', '¬']
_2args = ['AND', '&', '∧', 'OR', '|', '∨',
          'IMPLIES', '→', 'IFF', '↔', 'XOR', '⊕']

formula = []


def init(form: list):
    formula = form
    return analyse(formula)


def analyse(arr: list):
    """
    Funcion processes and prints tokens from imput
    with corresponding types.
    """

    print(arr)

    if len(arr) == 1:
        return f"{arr[0]}"

    else:
        token = arr.pop()

        if token in _quantifiers:
            formula = analyse(arr)
            variable = analyse(arr)
            return f"{token} {variable}. [{formula}]"

        elif token in _1args:
            arg_1 = analyse(arr)
            return f"{token} {arg_1}"

        elif token in _2args:
            arg_2 = analyse(arr)
            arg_1 = analyse(arr)
            return f"({arg_1}) {token} ({arg_2})"

        elif token.find('/') != -1:
            token = token.split('/')
            tmp_string = ""

            for arg in range(int(token.pop())):
                arg = analyse(arr)
                tmp_string += f"{arg},"

            tmp_string = tmp_string[:-1]
            return f"{token[0]}({tmp_string})"

        else:
            return f"{token}"

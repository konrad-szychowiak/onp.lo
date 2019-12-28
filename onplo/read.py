from onplo import type
from onplo import new_wrap as wrap


def get(form: str):
    """General parser function"""

    _formula = form.split()
    return analyse(_formula)


def analyse(data: list):
    """
    Function processes and prints tokens from input
    with corresponding types.
    """

    if len(data) == 0:
        raise IndexError("Out of reach")

    else:
        token = data.pop()

        if type.match("quantifier", token):
            formula = analyse(data)
            variable = analyse(data)
            return wrap.quantifier(token, variable, formula)

        elif type.match("single", token):
            arg = analyse(data)
            return wrap.single(token, arg)

        elif type.match("double", token):
            arg_2 = analyse(data)
            arg_1 = analyse(data)
            return wrap.double(token, arg_1, arg_2)

        elif type.rematch("predicate", token) or type.rematch("function", token):
            token, argc = token.split('/')
            term_list = ""

            for argv in range(int(argc)):
                argv = analyse(data)
                term_list = f"{argv}, " + term_list

            return wrap.predicate(token, term_list[:-2])

        elif type.rematch("constant", token) or type.rematch("variable", token):
            return token

        else:
            raise ValueError(f"""Forbidden token found whilst analysing given formula :
                '{token}' in position {len(data)}""")

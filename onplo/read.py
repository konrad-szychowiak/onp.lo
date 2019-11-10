import onpl.type as type
import onpl.wrap as wrap


_formula = []


def get(form: list):
    _formula = form

    try:
        answer = analyse(_formula)

    except (IndexError, ValueError) as Error:
        return f"[!] An error occured: {Error}"

    return answer


def analyse(arr: list):
    """
    Funcion processes and prints tokens from imput
    with corresponding types.
    """

    # print(arr)
    if len(arr) == 0:
        return ''

    else:
        token = arr.pop()

        if type.quantifier(token):
            formula = wrap._wrap(analyse(arr))
            variable = wrap._wrap(analyse(arr))
            return wrap.quantifier(token, variable, formula)

        elif type.single(token):
            arg = analyse(arr)
            return wrap.sngle(token, arg)

        elif type.double(token):
            arg_2 = analyse(arr)
            arg_1 = analyse(arr)
            return wrap.double(token, arg_1, arg_2)

        elif type.predicate(token) or type.function(token):
            token, argc = token.split('/')
            term_list = ""

            for argv in range(int(argc)):
                argv = analyse(arr)
                term_list = f"{argv}, " + term_list

            return wrap.predicate(token, term_list[:-2])

        elif type.constant(token) or type.variable(token):
            return token

        else:
            raise ValueError('Forbidden token found!')


def end(pre=False):
    if pre:
        print("")
    print("| \033[1;30mEXIT\033[0m")
